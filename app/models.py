from pydantic import BaseModel
from typing import Optional

class NewsResponse(BaseModel):
    title: str
    description: Optional[str]
    url: str
    source: str
    published_at: Optional[str]
