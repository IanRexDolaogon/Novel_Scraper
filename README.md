# Novel Scraper API (Local/VM Use Only)

* Requirements Before Starting
- Python 3.10 or higher
- Virtual environment (recommended)
- Internet connection for scraping

# steps
1. python -m venv venv (create a virtual env)
2. .\venv\Scripts\activate (if your on windows)
3. pip install fastapi uvicorn python-dotenv pyyaml google-cloud-translate requests beautifulsoup4 (install dependencies)
4. uvicorn app.main:app --reload
5. it run at http://127.0.0.1:8000

