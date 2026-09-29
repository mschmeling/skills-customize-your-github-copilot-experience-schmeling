# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI, practicing route creation, path and query parameters, Pydantic request validation, and HTTP status codes.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description

Complete the starter code to create a FastAPI application that responds to a health-check request.

#### Requirements

The completed program must:

- Create a `FastAPI` application instance.
- Implement a `GET /health` endpoint.
- Return `{"status": "ok"}` from the health-check endpoint.
- Start the application with Uvicorn so it can be tested locally.

### 🛠️ Implement book retrieval endpoints

#### Description

Add read-only endpoints for an in-memory collection of books. Clients should be able to retrieve every book or request one book by its ID.

#### Requirements

The completed program must:

- Store at least three books in an in-memory list.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return the matching book.
- Return HTTP status `404` when the requested book does not exist.
- Use the `category` query parameter to filter the collection when it is provided.

### 🛠️ Add validated book creation

#### Description

Create a request model with Pydantic and add an endpoint that validates and stores new books.

#### Requirements

The completed program must:

- Define a Pydantic model with required `title`, `author`, and `category` fields.
- Implement `POST /books` using the request model as its input.
- Add the new book to the in-memory collection with a unique ID.
- Return the created book with HTTP status `201`.
- Reject requests that omit a required field with FastAPI's validation response.

For example, a valid request body is:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "category": "Fantasy"
}
```
