import json
import os

import fire
from elasticsearch import Elasticsearch
from tqdm import tqdm


def main(file_name: str = "books.json"):
    with open(file_name, "r") as f:
        books = json.load(f)
    es = Elasticsearch(http_auth=("elastic", os.environ["ELASTICSEARCH_PW"]))
    for book in tqdm(books):
        book_item = book["Item"]
        try:
            es.create(index="book", id=book_item["isbn"], body=book_item)
        except Exception:
            pass


if __name__ == "__main__":
    fire.Fire(main)
