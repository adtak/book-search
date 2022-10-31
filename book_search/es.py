import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class ESClient:
    def __init__(self):
        self.client = Elasticsearch(
            "http://localhost:9200",
            http_auth=("elastic", os.environ["ELASTICSEARCH_PW"]),
        )

    def search(self, keyword, size):
        s = (
            Search(using=self.client, index="books")
            .query("match", **{"itemCaption": keyword})
            .extra(from_=0, size=size)
        )
        print(s.to_dict())
        response = s.execute()
        return [
            {"Title": i["_source"]["title"], "Score": i["_score"]}
            for i in response.hits.hits
        ]
