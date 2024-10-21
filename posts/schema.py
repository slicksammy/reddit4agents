from pydantic import BaseModel, EmailStr
import uuid
from typing import Optional

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