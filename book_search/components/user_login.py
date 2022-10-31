import streamlit as st
from book_search.db import get_db_conn
from book_search.user import User
from book_search.util import check_hashes, make_hashes


def login_component():
    st.subheader("Sign in")
    login_username = st.text_input("Login Username")
    login_password = st.text_input("Login Password", type="password")
    if st.button("Sign in"):
        db_conn = get_db_conn()
        user = User(db_conn)
        result = user.login_user(
            login_username, check_hashes(login_password, make_hashes(login_password))
        )
        if result:
            st.success(f"Login {login_username} Success.")
        else:
            st.warning("Login Fail.")
