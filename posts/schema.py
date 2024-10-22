from pydantic import BaseModel
import uuid
from typing import List, Optional
from datetime import datetime

class CreatePost(BaseModel):
    title: str
    body: str

class PostCreated(BaseModel):
    id: uuid.UUID

class CreateComment(BaseModel):
    body: str
    post_id: uuid.UUID
    parent_comment_id: Optional[uuid.UUID] = None

class CommentCreated(BaseModel):
    id: uuid.UUID

class Comment(BaseModel):
    id: uuid.UUID
    body: str
    post_id: uuid.UUID
    parent_id: Optional[uuid.UUID] = None
    level: int
    created_at: datetime
    children: List['Comment'] = []

class Post(BaseModel):
    id: uuid.UUID
    title: str
    body: str
    agent_id: uuid.UUID
    comments: List[Comment]

class Posts(BaseModel):
    posts: List[Post]