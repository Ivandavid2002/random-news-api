import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv("NEWS_API_URL")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY not found in environment variables")
