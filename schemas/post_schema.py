from pydantic import BaseModel


class Post(BaseModel):
    userId: int
    id: int = None
    title: str
    body: str
