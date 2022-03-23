# Analyzer

## Preparation

- 予めindex設定でkuromojiを指定する
```
PUT books
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "kuromoji_tokenizer"
        }
      }
    }
  }
}
```

- ユーザ辞書を登録する場合は以下のような形
```
PUT books
{
  "settings": {
    "index": {
      "analysis": {
        "tokenizer": {
          "kuromoji_user_dict": {
            "type": "kuromoji_tokenizer",
            "mode": "search",
            "user_dictionary_rules": ["関西国際空港,関西国際 空港,カンサイコクサイ クウコウ,カスタム名詞"]
          }
        },
        "analyzer": {
          "my_analyzer": {
            "type": "custom",
            "tokenizer": "kuromoji_user_dict"
          }
        }
      }
    }
  }
}
```

- mapping定義でanalyzerを指定
```
PUT books/_mapping
{
  "properties": {
    "title": {
      "type": "text",
      "analyzer": "my_analyzer",
      "search_analyzer": "my_analyzer"
    }
  }
}

GET books
```

```
PUT books/_doc/1
{
  "title": "関西国際空港"
}

PUT books/_doc/2
{
  "title": "関西にある国際空港"
}

PUT books/_doc/3
{
  "title": "関西 国際 空港"
}

PUT books/_doc/4
{
  "title": "国際空港"
}
```

## Search

```
GET books/_search
{
  "query": {
    "match": {
      "title": {
        "query": "関西国際空港",
        "analyzer": "my_analyzer"
      }
    }
  }
}
```

- ちなみにフィールド指定しない場合は以下
```
GET books/_search
{
  "query": {
    "simple_query_string": {
      "query": "関西国際空港",
      "fields": ["*"]
    }
  }
}
```

## Analyze

- index作成時のanalyze結果
```
GET books/_analyze
{
  "analyzer": "my_analyzer",
  "field": "title", 
  "text": "関西国際空港", 
  "explain": true
}
```

- クエリ発行時のanalyze結果
```
GET books/_validate/query?explain=true&rewrite=true
{
  "query": {
    "match": {
      "title": {
        "query": "関西国際空港",
        "analyzer": "my_analyzer"
      }
    }
  }
}
```

- クエリのスコアリング詳細
```
GET books/_explain/1
{
  "query": {
    "match": {
      "title": {
        "query": "関西国際空港",
        "analyzer": "my_analyzer"
      }
    }
  }
}
```

- inverted indexの確認
```
GET books/_doc/1/_termvectors
{
  "fields" : ["title"]
}
```
