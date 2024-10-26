from pydantic import BaseModel, field_validator

class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool

class User(BaseModel):
    name: str
    email: str
    membership_id: str

