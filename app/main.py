from fastapi import FastAPI

app = FastAPI(title="Novel Scraper & Translator by:IAN")

@app.get("/")
async def root():
    return {"message":"hello im making a webscraper as my personal hobby"}
