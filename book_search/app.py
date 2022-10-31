import streamlit as st
from book_search.db import get_db_conn
from book_search.user import User
from book_search.util import check_hashes, make_hashes
from dotenv import load_dotenv
from es import ESClient

db_conn = get_db_conn()
user = User(db_conn)
user.create_user()


def main_ui():
    keyword = st.text_input(label="", value="")
    return keyword


def side_ui():
    size = st.sidebar.number_input(label="件数", value=10, step=10)
    return size


def login_ui():
    st.subheader("Sign in")
    login_username = st.text_input("Login Username")
    login_password = st.text_input("Login Password", type="password")
    if st.button("Sign in"):
        result = user.login_user(
            login_username, check_hashes(login_password, make_hashes(login_password))
        )
        if result:
            st.success(f"Login {login_username} Success.")
        else:
            st.warning("Login Fail.")


def register_ui():
    st.subheader("Register")
    register_username = st.text_input("Register Username")
    register_password = st.text_input("Register Password", type="password")
    if st.button("Register"):
        user.add_user(register_username, make_hashes(register_password))
        st.success("Register Success.")


def main():
    st.markdown("## Book Search")
    login_ui()
    register_ui()
    keyword = main_ui()
    size = side_ui()
    es_client = ESClient()
    if st.button("検索"):
        st.dataframe(es_client.search(keyword, size))


if __name__ == "__main__":
    load_dotenv(".env")
    main()
