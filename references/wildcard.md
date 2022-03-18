# Wildcard

## PUT documents

```
PUT /memo/_doc/1
{
  "description": "This is a car."
}

PUT /memo/_doc/2
{
  "description": "This bike is made of carbon."
}
```

## Match

- 「This is」が形態素解析され、「text type」に対して検索するので2つともヒットする
```
GET /memo/_search
{
  "query": {
    "match": {
      "description": "This is"
    }
  }
}
```

- 「This is」は形態素解析されるが、「keyword type」に対して検索する(=index側は形態素解析されていない)のでヒットしない
```
GET /memo/_search
{
  "query": {
    "match": {
      "description.keyword": "This is"
    }
  }
}
```

## Term

- 「This is」は形態素解析されない。「text type」に対して検索するが「This is」というindexは存在しないのでヒットしない
```
GET /memo/_search
{
  "query": {
    "term": {
      "description": {
        "value": "This is"
      }
    }
  }
}
```

- 「This is」は形態素解析されない。「keyword type」も「This is」というindexは存在しないのでヒットしない
```
GET /memo/_search
{
  "query": {
    "term": {
      "description.keyword": {
        "value": "This is"
      }
    }
  }
}
```

## Wildcard

- 「This is」は形態素解析されない。ワイルドカードをつけても「text type」に「This is 〜」というindexは存在しないのでヒットしない
```
GET /memo/_search
{
  "query": {
    "wildcard": {
      "description": {
        "value": "This is"
      }
    }
  }
}

GET /memo/_search
{
  "query": {
    "wildcard": {
      "description": {
        "value": "This is*"
      }
    }
  }
}
```

- 「This is」は形態素解析されない。ワイルドカードをつけると「keyword type」には「This is a car.」というindexが存在するのでヒットする
```
GET /memo/_search
{
  "query": {
    "wildcard": {
      "description.keyword": {
        "value": "This is"
      }
    }
  }
}

GET /memo/_search
{
  "query": {
    "wildcard": {
      "description.keyword": {
        "value": "*This is*"
      }
    }
  }
}
```