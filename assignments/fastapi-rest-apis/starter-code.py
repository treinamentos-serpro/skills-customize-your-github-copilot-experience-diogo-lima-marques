from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]


@app.get("/books")
def list_books():
    raise NotImplementedError("Implement this endpoint")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    raise NotImplementedError("Implement this endpoint")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    raise NotImplementedError("Implement this endpoint")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    raise NotImplementedError("Implement this endpoint")