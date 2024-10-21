from pydantic import BaseModel, EmailStr
import uuid

class CreateAgent(BaseModel):
    name: str
    description: str
    email: EmailStr

class AgentCreated(BaseModel):
    id: uuid.UUID
    api_key: str