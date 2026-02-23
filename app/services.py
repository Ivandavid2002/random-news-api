import random
import requests
from .config import NEWS_API_KEY, NEWS_API_URL

def get_random_news(query: str = "technology"):
    params = {
        "q": query,
        "language": "en",
        "pageSize": 50,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code != 200:
        raise Exception("Error fetching news")

    articles = response.json().get("articles", [])

    if not articles:
        return None

    return random.choice(articles)
