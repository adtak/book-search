import streamlit as st
from dotenv import load_dotenv

from es import ESClient


def main_ui():
    keyword = st.text_input(label="", value="")
    return keyword


def side_ui():
    size = st.sidebar.number_input(label="件数", value=10, step=10)
    return size


def main():
    st.markdown("## Book Search")
    keyword = main_ui()
    size = side_ui()
    es_client = ESClient()
    if st.button("検索"):
        st.dataframe(es_client.search(keyword, size))


if __name__ == "__main__":
    load_dotenv(".env")
    main()
