# Virtual environment
VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Run Flask App
run:
	poetry run python main.py

# Run Tests
test:
	poetry run pytest

# Install Dependencies
install:
	$(PIP) install -r requirements.txt

# Create Virtual Environment
venv:
	python3 -m venv $(VENV)

# Activate Environment (Linux/Mac reminder)
activate:
	@echo "Run: source venv/bin/activate"

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
