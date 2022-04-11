from model import Todo
from model import Book

# MongoDB driver
import asyncio
import motor.motor_asyncio


async def get_server_info ():
    conn_str = "<mongodb://localhost:27017>"

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo
database2 = client.BookList
collection2 = database2.book


async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    await collection.update_one({"title":title},{"$set":{"description":desc}})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True

async def fetch_one_book(judul):
    document = await collection2.find_one({"judul":judul})
    return document

async def fetch_all_books():
    books = []
    cursor = collection2.find({})
    async for document in cursor:
        books.append(Book(**document))
    return books

async def create_book(book):
    document = book
    result = await collection2.insert_one(document)
    return document

async def update_book(judul, harga):
    await collection2.update_one({"judul":judul},{"$set":{"harga":harga}})
    document = await collection2.find_one({"judul":judul})
    return document

async def remove_book(judul):
    await collection2.delete_one({"judul":judul})
    return True