import streamlit as st
from es import ESClient


def search_component():
    keyword = st.text_input(label="", value="")
    size = st.number_input(label="件数", value=10, step=10)
    if st.button("検索"):
        es_client = ESClient()
        st.dataframe(es_client.search(keyword, size))
        es_client.client.close()
