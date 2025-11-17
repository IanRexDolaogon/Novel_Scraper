from fastapi import APIRouter, Query
from app.services.scraper_service import scrape_site, get_allowed_sites, ScraperError

router = APIRouter()

@router.get("/sites")
def list_sites():
    """Return all whitelisted domains."""
    return {"allowed_sites": get_allowed_sites()}

@router.get("/")
def scrape(url: str = Query(..., description="Full URL to scrape (must be whitelisted)")):
    """Scrape a page and return its main content."""
    try:
        content = scrape_site(url)
        return {"url": url, "content": content}
    except ScraperError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
