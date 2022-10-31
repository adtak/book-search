import streamlit as st
from book_search.components.book_search import search_component
from book_search.components.user_login import login_component
from book_search.components.user_register import register_component
from book_search.db import get_db_conn
from book_search.user import User
from dotenv import load_dotenv

db_conn = get_db_conn()
user = User(db_conn)
user.create_user()


def main():
    st.markdown("## Book Search")
    login_component()
    register_component()
    search_component()


if __name__ == "__main__":
    load_dotenv(".env")
    main()
