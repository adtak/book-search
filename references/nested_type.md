# Nested type

## Preparation

- 事前にnestedを指定しないとobjectになってしまう
```
DELETE /books

PUT /books
{
  "mappings": {
    "properties": {
      "reviews": {
        "type": "nested"
      }
    }
  }
}
```

- documentをPUTする
```
PUT /books/_doc/1
{
  "title": "test 1",
  "reviews": [{
    "name": "John",
    "detail": "good",
    "date": "2021-01-01"
  }, {
    "name": "Alice",
    "detail": "bad",
    "date": "2021-02-01"
  }]
}

PUT /books/_doc/2
{
  "title": "test 2",
  "reviews": [{
    "name": "David",
    "detail": "good and good",
    "date": "2021-01-01"
  }, {
    "name": "Mark",
    "detail": "bad",
    "date": "2021-02-01"
  }]
}

PUT /books/_doc/3
{
  "title": "test 3",
  "reviews": [{
    "name": "Mark",
    "detail": "good",
    "date": "2021-01-01"
  }, {
    "name": "Alice",
    "detail": "good and good",
    "date": "2021-02-01"
  }]
}

PUT /books/_doc/4
{
  "title": "test 4",
  "reviews": [{
    "name": "David",
    "detail": "good and bad",
    "date": "2021-02-01"
  }]
}

PUT /books/_doc/5
{
  "title": null,
  "reviews": [{
    "name": "Alice",
    "detail": "good and bad",
    "date": "2021-02-01"
  }]
}
```
```
GET /books/_search
{
  "query": {
    "match_all": {}
  }
}
```

## Search

- excludesで結果からreviewsを取り除ける
- nestedでreviewsを検索する。その時、pathで対象のnestedを指定する
- inner_hitsでnestedのスコアなども返却される
- score_modeで親にnestedのスコアをどうやって反映するか指定する
```
GET /books/_search
{
  "_source": {
    "excludes": "reviews"
  }, 
  "query": {
    "bool": {
      "must": [
        {
          "multi_match": {
            "query": "test",
            "fields": ["title"],
            "type": "best_fields"
          }
        },
        {
          "nested": {
            "path": "reviews",
            "query": {
              "bool": {
                "must": [
                  {
                    "match": {
                      "reviews.detail": "good"
                    }
                  },
                  {
                    "range": {
                      "reviews.date": {
                        "gte": "2021-01-15"
                      }
                    }
                  }
                ]
              }
            },
            "inner_hits": {},
            "score_mode": "avg"
          }
        }
      ]
    }
  }
}
```
