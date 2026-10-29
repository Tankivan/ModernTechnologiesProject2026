from pydantic import BaseModel, SecretStr
from datetime import datetime

class UserCreate(BaseModel):
    nickname: str
    password: SecretStr

class UserResponse(BaseModel):
    id: int
    nickname: str
    role: str

class PostCreateResponse(BaseModel):
    id: int
    owner_id: int
    content: str
    post_datetime: datetime