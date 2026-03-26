.PHONY: fmt lint install install-dev

install:
	poetry install

install-dev:
	poetry install --with dev

fmt:
	poetry run ruff format .

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check --fix .
