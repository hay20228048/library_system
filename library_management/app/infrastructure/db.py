# This file connects Flask with PostgreSQL.

# Main responsibilities:
# Create SQLAlchemy engine
# Load environment variables
# Provide Base metadata


from sqlalchemy import MetaData, create_engine

# Create Engine
# engine is used to Handles connection to PostgreSQL.
engine = create_engine(
    "postgresql://library_user:123456@library_db:5432/library_db",
    pool_pre_ping=True,  # checks connection before using it
    connect_args={},  # optional for Postgres
)

# Metadata object (used to store tables)
# metadata: SQLAlchemy Core uses this to register tables before creating them.

metadata = MetaData()


# Helper function to get connection
# I manually open and close DB connections.
def get_connection():
    return engine.connect()
