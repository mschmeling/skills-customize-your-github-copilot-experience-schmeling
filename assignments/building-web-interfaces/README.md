# 📘 Assignment: Building Web Interfaces with Streamlit

## 🎯 Objective

Build an interactive web interface using only Python and Streamlit. Practice page configuration, widgets, data presentation, and consuming data from the FastAPI application created in the previous assignment.

## 📝 Tasks

### 🛠️ Create the Streamlit page

#### Description

Complete the starter code to create the first version of a book dashboard.

#### Requirements

The completed program must:

- Configure the page with a title and a wide layout.
- Display a page title and a short description of the dashboard.
- Show the number of books using a Streamlit metric.
- Display the books in a readable table.
- Run locally with `streamlit run starter-code.py`.

### 🛠️ Add interactive filters

#### Description

Add Streamlit widgets so users can explore the book collection by category.

#### Requirements

The completed program must:

- Create a selection widget containing the available categories.
- Include an option that displays books from every category.
- Filter the displayed books when a category is selected.
- Update the book count to match the filtered results.
- Display a helpful message when a filter has no matching books.

### 🛠️ Connect the interface to the FastAPI service

#### Description

Replace the local book data with data fetched from the FastAPI API from the previous assignment.

#### Requirements

The completed program must:

- Request book data from `GET /books` using Python's `requests` library.
- Use a configurable API base URL with `http://127.0.0.1:8000` as the default.
- Show a clear error message when the API cannot be reached.
- Keep the category filter and book count working with API data.
- Avoid sending a new request on every unnecessary widget interaction by using Streamlit caching appropriately.

A successful dashboard should show the book count, category filter, and a table of books returned by the API.
