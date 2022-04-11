from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str

class Book(BaseModel):
    judul:str
    harga:str