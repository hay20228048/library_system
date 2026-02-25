# Virtual environment
VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Run Flask App
run:
	docker compose up

# Run Tests
test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff check . --fix

install:
	poetry install


# Clean Cache Files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
