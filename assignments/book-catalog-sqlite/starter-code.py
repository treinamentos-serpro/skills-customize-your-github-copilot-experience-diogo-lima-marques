import sqlite3
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API with SQLite")
DB_PATH = Path(__file__).with_name("books.db")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


@contextmanager
def connect_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_db():
    with connect_db() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
            """
        )
        book_count = connection.execute("SELECT COUNT(*) AS total FROM books").fetchone()["total"]
        if book_count == 0:
            connection.executemany(
                "INSERT INTO books (title, author) VALUES (?, ?)",
                [
                    ("Northbound", "Mira Chen"),
                    ("The Quiet Map", "Jordan Silva"),
                ],
            )


initialize_db()


@app.get("/books")
def list_books():
    raise NotImplementedError("Implement this endpoint")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    raise NotImplementedError("Implement this endpoint")


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    raise NotImplementedError("Implement this endpoint")


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    raise NotImplementedError("Implement this endpoint")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    raise NotImplementedError("Implement this endpoint")