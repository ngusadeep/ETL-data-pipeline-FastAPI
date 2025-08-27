from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from app.config import DATABASE_URL

def get_postgres_engine() -> Engine:
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set. Please check your .env file.")

    return create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20
    )
