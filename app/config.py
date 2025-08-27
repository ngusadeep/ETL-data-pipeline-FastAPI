import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# -------------------------
# Database configuration
# -------------------------
DATABASE_URL: str = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is missing in .env")

TABLE_NAME: str = os.getenv("TABLE_NAME") or "sales_table"

# -------------------------
# Raw data file path
# -------------------------
RAW_FILE_PATH: Path = Path(os.getenv("RAW_FILE_PATH") or "data/raw/sales_data.csv")

# -------------------------
# Scheduler configuration
# -------------------------
# Type: "interval" or "cron"
SCHEDULE_TYPE: str = os.getenv("SCHEDULE_TYPE") or "interval"

# Interval scheduling (minutes)
SCHEDULE_MINUTES: int = int(os.getenv("SCHEDULE_MINUTES") or 3)

# Cron scheduling (hour/minute)
SCHEDULE_HOUR: int = int(os.getenv("SCHEDULE_HOUR") or 2)
SCHEDULE_MINUTE: int = int(os.getenv("SCHEDULE_MINUTE") or 0)
