from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str =Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra" : {
            "example": {
                "title" : "A new book title",
                "author" : "Abhay",
                "description" : "New book",
                 "rating" : 3
            }
        }
    }











BOOKS = [
    Book(id=1, title="Book 1", author="Author 1", description="Description 1", rating=5),
    Book(id=2, title="Book 2", author="Author 2", description="Description 2", rating=4),
]


@app.get("/books")
async def read_books():
    return {"books": BOOKS}


@app.post("/create-book")
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