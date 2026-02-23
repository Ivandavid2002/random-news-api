from fastapi import FastAPI, HTTPException, Query
from .services import get_random_news
from .models import NewsResponse

app = FastAPI(
    title="Random News API",
    description="API that returns a random news article",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Random News API 🚀"}

@app.get("/news/random", response_model=NewsResponse)
def random_news(q: str = Query("technology", description="Keyword to search news")):
    article = get_random_news(q)

    if not article:
        raise HTTPException(status_code=404, detail="No news found")

    return {
        "title": article.get("title"),
        "description": article.get("description"),
        "url": article.get("url"),
        "source": article.get("source", {}).get("name"),
        "published_at": article.get("publishedAt")
    }
