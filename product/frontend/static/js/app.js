const API_BASE = "/api/v1";
let currentToken = localStorage.getItem("bb_token");
let currentUser = null;
let currentAlertId = null;

document.addEventListener("DOMContentLoaded", () => {
    if (currentToken) {
        loadMe();
    } else {
        showLogin();
    }
    setupEventListeners();
});

function setupEventListeners() {
    document.getElementById("login-form").addEventListener("submit", handleLogin);
    document.getElementById("logout-btn").addEventListener("click", handleLogout);
    document.getElementById("export-form").addEventListener("submit", handleExport);
    document.getElementById("scan-form").addEventListener("submit", handleScan);
    document.getElementById("alert-status-filter").addEventListener("change", loadAlerts);

    document.querySelectorAll("[data-page]").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            navigateTo(e.currentTarget.dataset.page);
        });
    });

    document.getElementById("btn-scan").addEventListener("click", () => {
        const modal = new bootstrap.Modal(document.getElementById("scan-modal"));
        modal.show();
    });

    document.getElementById("alert-action-progress").addEventListener("click", () => updateAlertStatus("en cours"));
    document.getElementById("alert-action-close").addEventListener("click", () => updateAlertStatus("cloturee"));
}

function showLogin() {
    document.getElementById("login-screen").classList.remove("d-none");
    document.getElementById("dashboard-screen").classList.add("d-none");
}

function showDashboard() {
    document.getElementById("login-screen").classList.add("d-none");
    document.getElementById("dashboard-screen").classList.remove("d-none");
    document.getElementById("user-display").textContent = currentUser.username;

    if (currentUser.role === "admin") {
        document.querySelectorAll(".btn-admin, .nav-item-admin").forEach(el => el.classList.remove("d-none"));
    }

    loadDashboard();
}

async function apiCall(url, options = {}) {
    const headers = { ...options.headers };
    if (currentToken) {
        headers["Authorization"] = `Bearer ${currentToken}`;
    }
    if (options.body && typeof options.body === "object" && !(options.body instanceof FormData)) {
        headers["Content-Type"] = "application/json";
        options.body = JSON.stringify(options.body);
    }

    const resp = await fetch(API_BASE + url, { ...options, headers });
    if (resp.status === 401) {
        handleLogout();
        throw new Error("Session expirée");
    }
    if (!resp.ok) {
        const err = await resp.json().catch(() => ({ detail: resp.statusText }));
        throw new Error(err.detail || resp.statusText);
    }
    return resp.json();
}

async function handleLogin(e) {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorEl = document.getElementById("login-error");

    try {
        const resp = await fetch(API_BASE + "/auth/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });
        if (!resp.ok) {
            const err = await resp.json();
            throw new Error(err.detail || "Identifiants invalides");
        }
        const data = await resp.json();
        currentToken = data.access_token;
        localStorage.setItem("bb_token", currentToken);
        errorEl.classList.add("d-none");
        loadMe();
    } catch (err) {
        errorEl.textContent = err.message;
        errorEl.classList.remove("d-none");
    }
}

function handleLogout() {
    currentToken = null;
    currentUser = null;
    localStorage.removeItem("bb_token");
    showLogin();
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
}

async function loadMe() {
    try {
        currentUser = await apiCall("/auth/me");
        showDashboard();
    } catch {
        showLogin();
    }
}

function navigateTo(page) {
    document.querySelectorAll(".page-content").forEach(el => el.classList.add("d-none"));
    document.querySelectorAll(".nav-link").forEach(el => el.classList.remove("active"));

    const pageEl = document.getElementById(`page-${page}`);
    if (pageEl) pageEl.classList.remove("d-none");

    document.querySelector(`[data-page="${page}"]`)?.classList.add("active");

    switch (page) {
        case "dashboard": loadDashboard(); break;
        case "compliance": loadCompliance(); break;
        case "assets": loadAssets(); break;
        case "alerts": loadAlerts(); break;
        case "traffic": loadTraffic(); break;
        case "exports": break;
        case "audit": loadAuditLogs(); break;
    }
}

async function loadDashboard() {
    try {
        const data = await apiCall("/dashboard/");
        const m = data.metrics;

        document.getElementById("metrics-cards").innerHTML = `
            <div class="col-md-3">
                <div class="card metric-card alerts">
                    <div class="card-body">
                        <div class="metric-value text-danger">${m.total_alerts}</div>
                        <div class="metric-label">Total alertes</div>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card metric-card assets">
                    <div class="card-body">
                        <div class="metric-value text-info">${m.total_assets}</div>
                        <div class="metric-label">Actifs d&eacute;couverts</div>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card metric-card audit">
                    <div class="card-body">
                        <div class="metric-value" style="color:#6f42c1">${m.total_audit_logs}</div>
                        <div class="metric-label">Entr&eacute;es d'audit</div>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card metric-card exports">
                    <div class="card-body">
                        <div class="metric-value text-success">${m.total_exports}</div>
                        <div class="metric-label">Exports g&eacute;n&eacute;r&eacute;s</div>
                    </div>
                </div>
            </div>
        `;

        const tbody = document.getElementById("recent-alerts-body");
        tbody.innerHTML = data.recent_alerts.map(a => `
            <tr>
                <td>${a.id}</td>
                <td>${a.title}</td>
                <td><span class="severity-${a.severity}">${a.severity}</span></td>
                <td><span class="status-${a.status.replace(" ", "-")}">${a.status}</span></td>
                <td><code>${a.source_ip || "-"}</code></td>
                <td>${formatDate(a.created_at)}</td>
            </tr>
        `).join("") || '<tr><td colspan="6" class="text-center text-muted">Aucune alerte</td></tr>';
    } catch (err) {
        console.error("Dashboard load failed:", err);
    }
}

async function loadAssets() {
    try {
        const response = await apiCall("/assets/");
        const assets = response.assets || [];
        const tbody = document.getElementById("assets-body");
        tbody.innerHTML = assets.map(a => `
            <tr>
                <td>${a.id}</td>
                <td><code>${a.ip_address}</code></td>
                <td>${a.hostname || "-"}</td>
                <td><span class="badge bg-${a.status === "active" ? "success" : "secondary"}">${a.status}</span></td>
                <td>${formatDate(a.first_seen_at)}</td>
                <td>${formatDate(a.last_seen_at)}</td>
                <td>
                    <button class="btn btn-sm btn-outline-info" onclick="viewAsset(${a.id})">
                        <i class="bi bi-eye"></i>
                    </button>
                </td>
            </tr>
        `).join("") || '<tr><td colspan="7" class="text-center text-muted">Aucun actif</td></tr>';
    } catch (err) {
        console.error("Assets load failed:", err);
    }
}

async function viewAsset(id) {
    try {
        const asset = await apiCall(`/assets/${id}`);
        const portsHtml = asset.ports.map(p =>
            `<span class="badge bg-secondary me-1">${p.port}/${p.protocol} ${p.service_name || ""}</span>`
        ).join("") || "Aucun port d&eacute;tect&eacute;";

        const modal = new bootstrap.Modal(document.getElementById("scan-modal"));
        document.querySelector("#scan-modal .modal-title").textContent = `Actif ${asset.ip_address}`;
        document.querySelector("#scan-modal .modal-body").innerHTML = `
            <p><strong>Hostname:</strong> ${asset.hostname || "-"}</p>
            <p><strong>Statut:</strong> ${asset.status}</p>
            <p><strong>Premi&egrave;re vue:</strong> ${formatDate(asset.first_seen_at)}</p>
            <p><strong>Derni&egrave;re vue:</strong> ${formatDate(asset.last_seen_at)}</p>
            <p><strong>Ports:</strong><br>${portsHtml}</p>
        `;
        document.querySelector("#scan-form").style.display = "none";
        modal.show();
        modal._element.addEventListener("hidden.bs.modal", () => {
            document.querySelector("#scan-form").style.display = "";
        }, { once: true });
    } catch (err) {
        console.error("Asset detail failed:", err);
    }
}

async function loadAlerts() {
    try {
        const filter = document.getElementById("alert-status-filter").value;
        let url = "/alerts/";
        if (filter) url += `?status=${filter}`;

        const response = await apiCall(url);
        const alerts = response.alerts || [];
        const tbody = document.getElementById("alerts-body");
        tbody.innerHTML = alerts.map(a => `
            <tr>
                <td>${a.id}</td>
                <td>${a.title}</td>
                <td><span class="severity-${a.severity}">${a.severity}</span></td>
                <td><span class="status-${a.status.replace(" ", "-")}">${a.status}</span></td>
                <td><code>${a.source_ip || "-"}</code></td>
                <td class="text-truncate" style="max-width:200px">${a.description || "-"}</td>
                <td>
                    <button class="btn btn-sm btn-outline-info" onclick="viewAlert(${a.id})">
                        <i class="bi bi-eye"></i>
                    </button>
                </td>
            </tr>
        `).join("") || '<tr><td colspan="7" class="text-center text-muted">Aucune alerte</td></tr>';
    } catch (err) {
        console.error("Alerts load failed:", err);
    }
}

async function viewAlert(id) {
    try {
        const alert = await apiCall(`/alerts/${id}`);
        currentAlertId = id;
        document.getElementById("alert-detail-body").innerHTML = `
            <p><strong>Titre:</strong> ${alert.title}</p>
            <p><strong>S&eacute;v&eacute;rit&eacute;:</strong> <span class="severity-${alert.severity}">${alert.severity}</span></p>
            <p><strong>Statut:</strong> <span class="status-${alert.status.replace(" ", "-")}">${alert.status}</span></p>
            <p><strong>Source IP:</strong> <code>${alert.source_ip || "-"}</code></p>
            <p><strong>Description:</strong> ${alert.description || "-"}</p>
            <p><strong>Cr&eacute;&eacute;e le:</strong> ${formatDate(alert.created_at)}</p>
        `;

        const btnProgress = document.getElementById("alert-action-progress");
        const btnClose = document.getElementById("alert-action-close");

        btnProgress.style.display = alert.status === "nouvelle" ? "" : "none";
        btnClose.style.display = (alert.status === "nouvelle" || alert.status === "en cours") ? "" : "none";

        const modal = new bootstrap.Modal(document.getElementById("alert-detail-modal"));
        modal.show();
    } catch (err) {
        console.error("Alert detail failed:", err);
    }
}

async function updateAlertStatus(status) {
    if (!currentAlertId) return;
    try {
        await apiCall(`/alerts/${currentAlertId}`, {
            method: "PATCH",
            body: { status },
        });
        bootstrap.Modal.getInstance(document.getElementById("alert-detail-modal")).hide();
        loadAlerts();
        loadDashboard();
    } catch (err) {
        alert("Erreur: " + err.message);
    }
}

async function handleExport(e) {
    e.preventDefault();
    const format = document.getElementById("export-format").value;
    const scope = document.getElementById("export-scope").value;

    try {
        const result = await apiCall("/exports/", {
            method: "POST",
            body: { format, scope },
        });

        document.getElementById("export-result").classList.remove("d-none");
        document.getElementById("export-message").textContent =
            `Export ${format.toUpperCase()} (${result.row_count} lignes) g&eacute;n&eacute;r&eacute; avec succ&egrave;s.`;
        document.getElementById("export-download-link").href = `/api/v1/exports/${result.id}/download`;
        document.getElementById("export-download-link").setAttribute("download", "");
    } catch (err) {
        alert("Erreur: " + err.message);
    }
}

async function handleScan(e) {
    e.preventDefault();
    const input = document.getElementById("scan-ip-start").value.trim();
    const errorEl = document.getElementById("scan-error");
    const successEl = document.getElementById("scan-success");

    errorEl.classList.add("d-none");
    successEl.classList.add("d-none");

    let startIp, endIp;

    if (input.includes("/")) {
        const [base, mask] = input.split("/");
        const bits = parseInt(mask, 10);
        if (isNaN(bits) || bits < 8 || bits > 32) {
            errorEl.textContent = "Masque CIDR invalide (utilise /8 à /32)";
            errorEl.classList.remove("d-none");
            return;
        }
        const parts = base.split(".").map(Number);
        const ipNum = (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3];
        const hostMask = 0xFFFFFFFF >>> bits;
        startIp = parts.join(".");
        const endNum = (ipNum | hostMask) & 0xFFFFFFFF;
        endIp = [(endNum >>> 24) & 0xFF, (endNum >>> 16) & 0xFF, (endNum >>> 8) & 0xFF, endNum & 0xFF].join(".");
    } else if (input.includes("-")) {
        const [s, e] = input.split("-").map(x => x.trim());
        startIp = s;
        endIp = e;
    } else {
        startIp = input;
        endIp = input;
    }

    try {
        const result = await apiCall("/scan/", {
            method: "POST",
            body: { start_ip: startIp, end_ip: endIp, ports: [22, 80, 443, 8080, 3306] },
        });
        successEl.textContent = `Scan termin\u00e9 : ${result.assets_found} actif(s), ${result.ports_scanned} port(s) scann\u00e9s en ${result.duration_seconds}s`;
        successEl.classList.remove("d-none");
        setTimeout(() => loadAssets(), 1000);
        loadDashboard();
    } catch (err) {
        errorEl.textContent = err.message;
        errorEl.classList.remove("d-none");
    }
}
}

async function loadAuditLogs() {
    try {
        const data = await apiCall("/audit-logs/");
        const tbody = document.getElementById("audit-body");
        tbody.innerHTML = data.logs.map(log => `
            <tr>
                <td>${log.id}</td>
                <td><code>${log.action}</code></td>
                <td>${log.target_type || "-"}</td>
                <td><span class="badge bg-${log.result.includes("error") || log.result.includes("denied") ? "danger" : "success"}">${log.result}</span></td>
                <td>${log.user_id ? `User #${log.user_id}` : "System"}</td>
                <td>${formatDate(log.created_at)}</td>
            </tr>
        `).join("") || '<tr><td colspan="6" class="text-center text-muted">Aucun journal</td></tr>';
    } catch (err) {
        console.error("Audit logs load failed:", err);
    }
}

async function loadTraffic() {
    try {
        const protocol = document.getElementById("traffic-protocol-filter").value;
        let url = "/traffic/?limit=200";
        if (protocol) url += `&protocol=${protocol}`;

        const data = await apiCall(url);
        const tbody = document.getElementById("traffic-body");
        tbody.innerHTML = data.captures.map(c => `
            <tr>
                <td>${c.id}</td>
                <td><code>${c.source_ip}</code></td>
                <td><code>${c.target_ip}</code></td>
                <td><span class="badge bg-info">${c.protocol.toUpperCase()}</span></td>
                <td>${c.source_port}</td>
                <td>${c.target_port}</td>
                <td class="text-truncate" style="max-width:200px">${c.payload_summary || "-"}</td>
                <td>${formatDate(c.timestamp)}</td>
            </tr>
        `).join("") || '<tr><td colspan="8" class="text-center text-muted">Aucun trafic captur&eacute;</td></tr>';
    } catch (err) {
        console.error("Traffic load failed:", err);
    }
}

function formatDate(iso) {
    if (!iso) return "-";
    const d = new Date(iso);
    return d.toLocaleDateString("fr-FR") + " " + d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
}

async function loadCompliance() {
    try {
        const data = await apiCall("/compliance/nis2");
        const score = data.score;

        document.getElementById("nis2-score").textContent = `${score.overall_score}%`;
        document.getElementById("nis2-conform").textContent = score.compliant_count;
        document.getElementById("nis2-partial").textContent = score.partial_count;
        document.getElementById("nis2-nonconform").textContent = score.non_compliant_count;
        document.getElementById("nis2-total").textContent = score.total_requirements;

        const tbody = document.getElementById("nis2-requirements-body");
        tbody.innerHTML = data.requirements.map(r => {
            let badgeClass = "bg-danger";
            let badgeText = "Non conforme";
            if (r.status === "conforme") {
                badgeClass = "bg-success";
                badgeText = "Conforme";
            } else if (r.status === "partiellement_conforme") {
                badgeClass = "bg-warning text-dark";
                badgeText = "Partiel";
            }
            return `
                <tr>
                    <td><code>${r.id}</code></td>
                    <td><strong>${r.title}</strong><br><small class="text-muted">${r.description}</small></td>
                    <td><span class="badge ${badgeClass}">${badgeText}</span></td>
                    <td>${r.evidence || "-"}</td>
                    <td>${r.recommendation || '<span class="text-success"><i class="bi bi-check"></i></span>'}</td>
                </tr>
            `;
        }).join("");
    } catch (err) {
        console.error("Compliance load failed:", err);
    }
}
