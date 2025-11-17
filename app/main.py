from fastapi import FastAPI
from app.services.translate_service import translate_text
from app.routers import scraper_router

app = FastAPI(title="Novel Scraper & Translator by:IAN")

app.include_router(scraper_router.router, prefix="/scrape", tags=["Scraper"])

@app.get("/test-translate")
def test_translate():
    original ="你好世界"
    translated = translate_text(original)
    return {"original": original, "translated": translated}

