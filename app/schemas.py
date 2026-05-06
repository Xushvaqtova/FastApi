
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# ... (avvalgi schemalar)

# ─── TOKEN SCHEMAS ────────────────────────────

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

    
class Category(BaseModel):
    name: str
    description: str

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    category_id: Optional[int] = None

class PostUpdate(PostBase):
    pass  # used when updating a post (same fields)

class PostResponse(PostBase):
    id: int                 # comes from DB
    created_at: datetime    # timestamp from DB
    owner_id: Optional[int] = None  # may be None

    class Config:
        from_attributes = True  # allows reading from ORM (DB model)




class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True