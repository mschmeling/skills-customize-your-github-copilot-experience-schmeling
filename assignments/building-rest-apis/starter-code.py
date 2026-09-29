from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Library API")

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "category": "Classic"},
    {"id": 3, "title": "The Hobbit", "author": "J. R. R. Tolkien", "category": "Fantasy"},
]


class BookCreate(BaseModel):
    title: str
    author: str
    category: str


@app.get("/health")
def health_check():
    # TODO: Return the API health status.
    pass


@app.get("/books")
def list_books(category: str | None = None):
    # TODO: Return every book, or only books in the requested category.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find a book by ID and raise HTTPException with status 404 if it is missing.
    pass


@app.post("/books", status_code=201)
def create_book(book_data: BookCreate):
    # TODO: Create a unique ID, add the new book to the collection, and return it.
    pass


# Run with: uvicorn starter-code:app --reload
