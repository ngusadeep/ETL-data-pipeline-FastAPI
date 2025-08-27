from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
# Load .env file
load_dotenv()

# Get Neon connection string
DATABASE_URL = os.getenv("DATABASE_URL")

def get_postgres_engine():
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in .env")
    return create_engine(DATABASE_URL)
