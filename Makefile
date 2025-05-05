install:
	poetry install --sync
	poetry run pre-commit install

test:
	poetry run pytest .

code-quality:
	poetry run ruff check . --fix
	poetry run ruff format .
	poetry run mypy .

check-code-quality:
	poetry run ruff check .
	poetry run ruff format --check .
	poetry run mypy .

precommit:
	poetry run pre-commit run --all-files