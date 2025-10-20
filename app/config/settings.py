from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GOOGLE_APPLICATION_CREDENTIALS: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    SCRAPER_USER_AGENT: str = os.getenv("SCRAPER_USER_AGENT")
    SCRAPER_TIMEOUT: int = int(os.getenv("SCRAPER_TIMEOUT",10))
    APP_NAME: str = os.getenv("APP_NAME", "Novel Scraper")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()