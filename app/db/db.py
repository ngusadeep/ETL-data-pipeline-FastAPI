from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from app.config import DATABASE_URL

def get_postgres_engine() -> Engine:
    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL is not set in the environment")
    return create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20
    )
