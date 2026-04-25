from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    quantity: float = Field(..., ge=0, le=10000)
    category: str = Field(..., min_length=1)

class ItemOut(BaseModel):
    id: int
    name: str
    quantity: float
    category: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str