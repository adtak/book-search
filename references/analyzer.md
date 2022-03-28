# Analyzer

## Preparation

- 予めindex設定でkuromojiを指定する。ユーザ辞書とシノニムを登録する場合は以下のような形
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
            "user_dictionary_rules": ["関東国際空港,関東国際空港,カントウコクサイクウコウ,カスタム名詞"]
          }
        },
        "filter": {
          "search_synonym": {
            "type": "synonym_graph",
            "synonyms": ["関東国際空港 => 関東国際空港, 関東 国際 空港"]
          }
        },
        "analyzer": {
          "my_index_analyzer": {
            "type": "custom",
            "tokenizer": "kuromoji_user_dict"
          },
          "my_search_analyzer": {
            "type": "custom",
            "tokenizer": "kuromoji_user_dict",
            "filter": ["search_synonym"]
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
      "analyzer": "my_index_analyzer",
      "search_analyzer": "my_search_analyzer"
    }
  }
}

GET books
```

```
PUT books/_doc/1
{
  "title": "関東国際空港"
}

PUT books/_doc/2
{
  "title": "関東にある国際空港"
}

PUT books/_doc/3
{
  "title": "関東 国際 空港"
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
        "query": "関東国際空港",
        "auto_generate_synonyms_phrase_query": "false"
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
  "analyzer": "my_index_analyzer",
  "field": "title", 
  "text": "関東国際空港", 
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
        "query": "関東国際空港",
        "auto_generate_synonyms_phrase_query": "false"
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
        "query": "関西国際空港"
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
