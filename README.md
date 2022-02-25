# book-search

## Setup

```sh
$ docker-compose up -d
```
```sh
$ docker exec -it elasticsearch /bin/bash
```
```sh
$ bin/elasticsearch-setup-passwords auto
```
```sh
$ docker exec -it kibana /bin/bash
```
```sh
$ vi config/kibana.yml
elasticsearch.username: "kibana"
elasticsearch.password: "PASSWORD"
```