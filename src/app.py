import os

import streamlit as st
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


def main_ui():
    keyword = st.text_input(label="", value="")
    return keyword


def side_ui():
    size = st.sidebar.number_input(label="件数", value=10, step=10)
    return size


def main():
    st.markdown("## Book Search")
    keyword = main_ui()
    _ = side_ui()
    client = Elasticsearch(
        "http://localhost:9200", http_auth=("elastic", os.environ["ELASTICSEARCH_PW"])
    )
    if st.button("検索"):
        s = Search(using=client, index="book").query(
            "match", **{"itemCaption": keyword}
        )
        print(s.to_dict())
        response = s.execute()
        results = [
            {"Title": i["_source"]["title"], "Score": i["_score"]}
            for i in response.hits.hits
        ]
        st.dataframe(results)


if __name__ == "__main__":
    main()
