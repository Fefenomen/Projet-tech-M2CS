"""i18n — Translation API router."""

from typing import Optional

from fastapi import APIRouter, Query

from .service import get_translations, get_translation, SUPPORTED_LANGUAGES

router = APIRouter(prefix="/i18n", tags=["i18n"])


@router.get("/supported")
async def get_supported_languages():
    """Get list of supported languages."""
    return {"languages": list(SUPPORTED_LANGUAGES), "default": "fr"}


@router.get("/{lang}")
async def get_language_translations(
    lang: str,
    section: Optional[str] = Query(None, description="Filter by section (e.g. dashboard, alerts)"),
):
    """Get translations for a language.

    - **lang**: Language code (fr, en)
    - **section**: Optional section filter
    """
    if lang not in SUPPORTED_LANGUAGES:
        lang = "fr"

    translations = get_translations(lang)

    if section and section in translations:
        return {lang: translations[section]}

    return {lang: translations}


@router.get("/{lang}/{key}")
async def get_specific_translation(
    lang: str,
    key: str,
):
    """Get a specific translation key.

    - **lang**: Language code (fr, en)
    - **key**: Dot-notation key (e.g. dashboard.title)
    """
    if lang not in SUPPORTED_LANGUAGES:
        lang = "fr"

    value = get_translation(lang, key)
    return {"lang": lang, "key": key, "value": value}
