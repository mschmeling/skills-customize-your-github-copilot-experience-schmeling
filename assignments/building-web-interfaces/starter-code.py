import requests
import streamlit as st

LOCAL_BOOKS = [
    {"id": 1, "title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "category": "Classic"},
    {"id": 3, "title": "The Hobbit", "author": "J. R. R. Tolkien", "category": "Fantasy"},
]

st.set_page_config(page_title="Book Dashboard", layout="wide")

st.title("Book Dashboard")
st.write("Explore the books available in the library.")


@st.cache_data
def load_books(api_url):
    # TODO: Request the books from the API and return the JSON list.
    return LOCAL_BOOKS


api_url = st.sidebar.text_input("API base URL", "http://127.0.0.1:8000")

try:
    books = load_books(f"{api_url}/books")
except requests.RequestException:
    st.error("The book API could not be reached. Start the FastAPI server and try again.")
    books = LOCAL_BOOKS

categories = sorted({book["category"] for book in books})
selected_category = st.sidebar.selectbox("Category", ["All"] + categories)

# TODO: Filter books using selected_category.
filtered_books = books

st.metric("Books", len(filtered_books))

if filtered_books:
    st.dataframe(filtered_books, use_container_width=True)
else:
    st.info("No books match the selected category.")

# Run with: streamlit run starter-code.py
