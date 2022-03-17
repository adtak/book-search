import os
from pprint import pprint

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q, Search
from elasticsearch_dsl.response import Response


def main():
    client = Elasticsearch(
        "http://localhost:9200",
        http_auth=("elastic", os.environ["ELASTICSEARCH_PW"]),
    )
    _, index = "good", "books"
    s = (
        Search(using=client, index=index)
        .query("match", **{"title": "test"})
        .query(
            "nested",
            path="reviews",
            score_mode="avg",
            inner_hits={},
            query=Q(
                "bool",
                must=[
                    Q("match", **{"reviews.detail": "good"}),
                    Q("range", **{"reviews.date": {"gte": "2021-01-15"}}),
                ]
            )
        )
    )
    pprint(s.to_dict())
    response: Response = s.execute()
    pprint(f"--- Results: {len(response.hits.hits)} ---")
    pprint(response.hits.hits)


if __name__ == "__main__":
    main()
