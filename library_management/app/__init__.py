# Import tables to register them so metadata knows them
from fastapi import FastAPI

from app.domain.models import book as book  # (Register Tables)
from app.domain.models import member as member
from app.infrastructure.db import engine, metadata


def create_app():
    
    app = FastAPI()

    # Create tables automatically
    metadata.create_all(engine)

    return app