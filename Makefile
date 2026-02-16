# Virtual environment
VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Run Flask App
run:
	$(PYTHON) main.py

# Run Tests
test:
	PYTHONPATH=. pytest -v

# Install Dependencies
install:
	$(PIP) install -r requirements.txt

# Create Virtual Environment
venv:
	python3 -m venv $(VENV)

# Activate Environment (Linux/Mac reminder)
activate:
	@echo "Run: source venv/bin/activate"

# Freeze Dependencies
freeze:
	$(PIP) freeze > requirements.txt

# Clean Cache Files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
