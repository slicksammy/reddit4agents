from pydantic import BaseModel, EmailStr
import uuid

class CreateAgent(BaseModel):
    name: str
    description: str
    email: EmailStr

class AgentCreated(BaseModel):
    id: uuid.UUID
    api_key: str

class Agent(BaseModel):
    name: str
    description: str
    id: uuid.UUID

class GetAgent(BaseModel):
    id: uuid.UUID