# book-search

ElasticSearch and Streamlit

## ElasticStack

### Running

```sh
$ docker-compose up -d
```

### Setting ElasticSearch

```sh
$ docker exec -it elasticsearch /bin/bash
```
```sh
$ bin/elasticsearch-setup-passwords auto
```

### Setting Kibana

```sh
$ docker exec -it kibana /bin/bash
```
```sh
$ vi config/kibana.yml
elasticsearch.username: "kibana"
elasticsearch.password: "YOUR_PASSWORD"
```

## ETL

```sh
$ poetry run python ./src/get_books.py
$ poetry run python ./src/load_books.py
```

## UI

```sh
$ poetry run streamlit run ./src/app.py
```