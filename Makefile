.PHONY: format black isort test start

format: black isort

black:
				poetry run black .

isort:
				poetry run isort .

test:
				poetry run pytest

start:
				poetry run streamlit run ./book_search/app.py
