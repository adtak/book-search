import json

import fire
from es import ESClient
from tqdm import tqdm


def main(file_name: str = "books.json"):
    with open(file_name, "r") as f:
        books = json.load(f)
    client = ESClient()
    for book in tqdm(books):
        book_item = book["Item"]
        try:
            client.create(index="books", id=book_item["isbn"], body=book_item)
        except Exception:
            pass


if __name__ == "__main__":
    fire.Fire(main)
