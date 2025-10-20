from google.cloud import translate_v2 as translate
from app.config.settings import settings

def translate_text(text: str, target_language: str = "en"):
    """Translate any text to english by default"""
    client = translate.Client.from_service_account_json(settings.GOOGLE_APPLICATION_CREDENTIALS)
    result = client.translate(text, target_language=target_language)
    return result["translatedText"]