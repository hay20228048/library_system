#This file connects Flask with PostgreSQL.

#Main responsibilities:
    # Create SQLAlchemy engine
    # Create session
    # Load environment variables
    # Provide Base metadata


 
#I will Use because of SQLAlchemy Core:

#Table
#engine.connect()
#insert(), select(), update(), delete()
#metadata


from sqlalchemy import create_engine, MetaData 
from config import Config


# Create Engine
# engine is used to Handles connection to PostgreSQL.
engine = create_engine(Config.DATABASE_URL, echo=True) #
# Metadata object (used to store tables)
#metadata: SQLAlchemy Core uses this to register tables before creating them.

metadata = MetaData()


# Helper function to get connection
#I manually open and close DB connections.
def get_connection():
    return engine.connect()
