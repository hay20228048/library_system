# Import tables to register them so metadata knows them
from app.domain.models import book as book  # (Register Tables)
from app.domain.models import member as member
from app.infrastructure.db import engine, metadata
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Create tables automatically
    metadata.create_all(engine)

    return app