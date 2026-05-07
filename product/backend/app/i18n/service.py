"""i18n — Translation service."""

import json
import os
from typing import Optional

I18N_DIR = os.path.dirname(os.path.abspath(__file__))
SUPPORTED_LANGUAGES = {"fr", "en"}
DEFAULT_LANGUAGE = "fr"

_cache: dict[str, dict] = {}


def _load_language(lang: str) -> dict:
    if lang in _cache:
        return _cache[lang]

    file_path = os.path.join(I18N_DIR, f"{lang}.json")
    if not os.path.exists(file_path):
        file_path = os.path.join(I18N_DIR, f"{DEFAULT_LANGUAGE}.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    _cache[lang] = data
    return data


def get_translations(lang: str) -> dict:
    """Get all translations for a language."""
    if lang not in SUPPORTED_LANGUAGES:
        lang = DEFAULT_LANGUAGE
    return _load_language(lang)


def get_translation(lang: str, key: str, default: Optional[str] = None) -> str:
    """Get a specific translation key."""
    translations = get_translations(lang)
    parts = key.split(".")
    current = translations
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return default or key
    return current if isinstance(current, str) else (default or key)
