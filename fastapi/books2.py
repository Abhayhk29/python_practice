# The three biggest are:

# .dict() function is now renamed to .model_dump()

# schema_extra function within a Config class is now renamed to json_schema_extra

# Optional variables need a =None example: id: Optional[int] = None

from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publish_date: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, publish_date: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str =Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    publish_date: int = Field(gt=1999, lt=2031)
    model_config = {
        "json_schema_extra" : {
            "example": {
                "title" : "A new book title",
                "author" : "Abhay",
                "description" : "New book",
                 "rating" : 3,
                 "publish_date" : 2023,
            }
        }
    }


BOOKS = [
    Book(id=1, title="Book 1", author="Author 1", description="Description 1", rating=5, publish_date=2020),
    Book(id=2, title="Book 2", author="Author 2", description="Description 2", rating=4, publish_date=2021),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_books():
    return {"books": BOOKS}


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_books(book_id : int = Path(gt=0, description="The ID of the book to retrieve")):
    for book in BOOKS:
        if book.id == book_id:
            return {"book": book}
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")    
    # return {"error": "Book not found"}

@app.get("/books/publish_date/{publish_date}", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(publish_date: int = Path(gt=1999, lt=2031, description="The publish date of the book to retrieve")):
    for book in BOOKS:
        if book.publish_date == publish_date:
            return {"book": book}
    raise HTTPException(status_code=404, detail=f"Book with publish date {publish_date} not found")

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_title(rating: int = Query(gt=-1, lt=6, description="The rating of the book to retrieve")):
    for book in BOOKS:
        if book.rating == rating:
            return {"book": book}
    raise HTTPException(status_code=404, detail=f"Book with rating {rating} not found")

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    print(type(book_request))
    # new_book = Book(**book_request.dict())
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))
    return {"message": "Book created successfully", "book": book_request}



def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1;
    # else:
    #     book.id = 1

    return book


@app.put("/update-book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_id: int, book_request: BookRequest):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            updated_book = Book(**book_request.model_dump())
            updated_book.id = book_id
            BOOKS[index] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


@app.delete("/delete-book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0, description="The ID of the book to delete")):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            del BOOKS[index]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")