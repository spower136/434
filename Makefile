setup:
	python3 -m venv ~/.434

install:
	pip3 install -r requirements.txt

test:
	python -m pytest -vv --cov=myrepolib  tests/*.py
	# python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C myrepolib

all: setup install test lint
