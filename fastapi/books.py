# uvicorn books:app --reload
# fastapi run books.py  production mode
#fastapi dev books.py dev mode
# python m venv fastapienv
# pip install "uvicorn[standard]"
# deactivate for deactivate the environment
# .\fastapienv\Scripts\activate.bat
#  python -m uvicorn books:app --reload
from fastapi import Body, FastAPI

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
    print("Reading all books")
    return {"books": books}

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    print(book_id)
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

@app.get("/books/{book_id}/{book_title}")
async def read_book_by_id_and_title(book_id: int, book_title: str):
    for book in books:
        if book["id"] == book_id and book["title"] == book_title:
            return {"book": book}
    return {"error": "Book not found"}

# if urls seems to be same then the order of the urls matters, the first one will be executed first and the second one will be ignored
# cnstant will be executed first and the second one will be ignored

# query paramaters
@app.get("/book/search")
async def search_books(author: str , title: str = None):
    results = []
    for book in books:
        if author and title:
            if book["author"].casefold() == author.casefold() and book["title"].casefold() == title.casefold():
                results.append(book)
        elif author:
            if book["author"].casefold() == author.casefold():
                results.append(book)
        elif title:
            if book["title"].casefold() == title.casefold():
                results.append(book)
    return {"results": results}



@app.post("/books/create_book")
async def create_book(new_book = Body(...)):
    books.append(new_book)
    return {"message": "new book added successfully"}

@app.put("/books/update_book/{book_id}")
async def update_book(book_id: int, updated_book = Body(...)):
    for book in books:
        if book["id"] == book_id:
            book.update(updated_book)
            return {"message": "book updated successfully"}
    return {"error": "Book not found"}


@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for book in books:
        if book.get("id") == book_id:
            books.remove(book)
            return {"message": "book deleted successfully"}
    return {"error": "Book not found"}
