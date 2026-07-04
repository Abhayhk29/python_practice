# uvicorn books:app --reload
# fastapi run books.py  production mode
#fastapi dev books.py dev mode
from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
    {"id": 4, "title": "Book 4", "author": "Author 4"},
    {"id": 5, "title": "Book 5", "author": "Author 5"},
    {"id": 6, "title": "Book 6", "author": "Author 6"},
]

@app.get("/books")
async def read_books():
    return {"books": books}


@app.get("/books/mybook")
async def create_book():
    # books.append(book)
    return {"message": "new book added successfully"}

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"book": book}
    return {"error": "Book not found"}

@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in books:
        if book["title"] == book_title:
            return {"book": book}
    return {"error": "Book not found"}