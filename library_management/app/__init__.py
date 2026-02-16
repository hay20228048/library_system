from flask import Flask
from app.infrastructure.db import engine, metadata

# Import tables to register them so metadata knows them
from app.domain.models import book, member #(Register Tables)

def create_app():
    app = Flask(__name__)

    # Create tables automatically
    metadata.create_all(engine)

    return app