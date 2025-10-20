from fastapi import FastAPI
from app.services.translate_service import translate_text

app = FastAPI(title="Novel Scraper & Translator by:IAN")

@app.get("/")
async def root():
    return {"message":"hello im making a webscraper as my personal hobby"}

@app.get("/test-translate")
def test_translate():
    original ="你好世界"
    translated = translate_text(original)
    return {"original": original, "translated": translated}
