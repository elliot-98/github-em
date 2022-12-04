install:
	poetry install
	pre-commit install

test:
	poetry run pytest .

code-quality:
	poetry run black .
	poetry run isort . --recursive
	poetry run flake8 .
	poetry run mypy .

check-code-quality:
	poetry run black --check .
	poetry run isort . --recursive --check-only
	poetry run flake8 .
	poetry run mypy .
