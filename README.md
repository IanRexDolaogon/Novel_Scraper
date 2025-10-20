# only runs on a vm this is how you set it up
1. python -m venv venv
2. .\venv\Scripts\activate (windows)
3. pip install fastapi uvicorn python-dotenv pyyaml google-cloud-translate requests beautifulsoup4
4. pip freeze > requirements.txt 
5. then run - uvicorn app.main:app --reload

