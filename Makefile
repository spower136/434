setup:
	python3 -m venv ~/.434

install:
	pip3 install -r requirements.txt

test:
	python -m pytest -vv --cov=fruitlib  main.py
	# python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C fruitlib

all: setup install test lint
