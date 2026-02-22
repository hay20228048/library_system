FROM python:3.13-slim

WORKDIR /app

# install system deps
RUN apt-get update && apt-get install -y gcc

# copy dependency files first (cache optimization)
COPY pyproject.toml poetry.lock* ./

# install poetry
RUN pip install poetry

# install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root




# copy project
COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]