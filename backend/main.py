from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from model import Book

#App Object
app = FastAPI()

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
    fetch_one_book,
    fetch_all_books,
    create_book,
    update_book,
    remove_book,
)

origins = ['https://localhost:3000','http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def read_root():
    return {"Ping":"Pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    print(response)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(title, desc)
    print(response)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    print(response)
    if response:
        return "succesfully deleted todo item !"
    raise HTTPException(404, f"there is no TODO item with this title {title}")

@app.get("/api/book")
async def get_book():
    response = await fetch_all_books()
    return response

@app.get("/api/book/{judul}", response_model=Book)
async def get_book_by_judul(judul):
    response = await fetch_one_book(judul)
    print(response)
    if response:
        return response
    raise HTTPException(404, f"there is no BOOK item with this title {judul}")

@app.post("/api/book", response_model=Book)
async def post_book(book:Book):
    response = await create_book(book.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")

@app.put("/api/book/{judul}", response_model=Book)
async def put_book(judul:str, harga:str):
    response = await update_book(judul, harga)
    print(response)
    if response:
        return response
    raise HTTPException(404, f"there is no BOOK item with this title {judul}")

@app.delete("/api/book/{judul}")
async def delete_book(judul):
    response = await remove_book(judul)
    print(response)
    if response:
        return "succesfully deleted book item !"
    raise HTTPException(404, f"there is no BOOK item with this title {judul}")

