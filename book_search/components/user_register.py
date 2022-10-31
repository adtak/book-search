import streamlit as st
from book_search.db import get_db_conn
from book_search.user import User
from book_search.util import make_hashes


def register_component():
    st.header("Register")
    register_username = st.text_input("Register Username")
    register_password = st.text_input("Register Password", type="password")
    if st.button("Register"):
        db_conn = get_db_conn()
        user = User(db_conn)
        user.add_user(register_username, make_hashes(register_password))
        db_conn.close()
        st.success("Register Success.")
