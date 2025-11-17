import requests
from bs4 import BeautifulSoup
import yaml
import os
from app.config.settings import settings

class ScraperError(Exception):
    """Custom error for scraper issues."""
    pass

def load_sites():
    try:
        with open(os.path.join("app", "config", "sites.yaml"), "r", encoding="utf-8") as f:
            return yaml.safe_load(f)["allowed_sites"]
    except Exception as e:
        raise ScraperError(f"Failed to load site configuration: {str(e)}")

ALLOWED_SITES = load_sites()

def get_allowed_sites():
    return [site["domain"] for site in ALLOWED_SITES]

def find_site_config(url: str):
    for site in ALLOWED_SITES:
        if site["domain"] in url:
            return site
    raise ScraperError("Website not allowed or not found in whitelist.")

def scrape_site(url: str) -> str:
    """Scrape text from a whitelisted site with full error handling."""
    try:
        site = find_site_config(url)
    except ScraperError:
        raise

    headers = {"User-Agent": settings.SCRAPER_USER_AGENT}

    try:
        response = requests.get(url, headers=headers, timeout=settings.SCRAPER_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise ScraperError("Request timed out — site is too slow.")
    except requests.exceptions.ConnectionError:
        raise ScraperError("Connection error — site unreachable.")
    except requests.exceptions.HTTPError as e:
        raise ScraperError(f"HTTP error: {e.response.status_code}")
    except Exception as e:
        raise ScraperError(f"Unexpected request error: {str(e)}")

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        selector = site.get("content_selector")
        if not selector:
            raise ScraperError("Selector missing in site config.")

        element = soup.select_one(selector)
        if not element:
            raise ScraperError(f"Content not found using selector: {selector}")

        return element.get_text(strip=True)

    except Exception as e:
        raise ScraperError(f"Parsing error: {str(e)}")
