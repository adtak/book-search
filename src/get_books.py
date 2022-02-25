import json
import os
import time

import fire
import requests

API_URL = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"


def get_books(keyword: str, file_name: str = "books.json"):
    payload = {
        "format": "json",
        "applicationId": os.environ["RAKUTEN_APP_ID"],
        "booksGenreId": "000",
        "keyword": keyword,
        "page": 1,
    }
    books = []
    while True:
        response = requests.get(API_URL, params=payload)
        data = json.loads(response.text)
        books.extend(data["Items"])
        if data["pageCount"] == data["page"]:
            break
        payload["page"] = data["page"] + 1
        time.sleep(1)
    with open(file_name, "w") as f:
        json.dump(books, f)


if __name__ == "__main__":
    fire.Fire(get_books)
