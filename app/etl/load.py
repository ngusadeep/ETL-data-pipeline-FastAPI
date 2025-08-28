from sqlalchemy import text
import pandas as pd
from sqlalchemy.engine import Engine
from app.config import TABLE_NAME
from app.utils.logger import logger

def load_data_to_db(df: pd.DataFrame, table_name: str = TABLE_NAME, engine: Engine = None) -> int:
    """Load DataFrame into PostgreSQL, avoiding duplicates."""
    if df.empty:
        logger.info("No data to load.")
        return 0

    # Always normalize column names
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Get existing rows (normalized)
    with engine.connect() as conn:
        existing = pd.read_sql(
            text(f"SELECT sales_amount, unit_price, unit_cost FROM {table_name}"), 
            conn
        )
        existing.columns = [col.lower().replace(" ", "_") for col in existing.columns]

    # Merge to keep only new rows
    if not existing.empty:
        merged = pd.merge(
            df, 
            existing, 
            on=['sales_amount', 'unit_price', 'unit_cost'], 
            how='left', 
            indicator=True
        )
        new_rows = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])
    else:
        new_rows = df

    # Insert only new rows
    if not new_rows.empty:
        new_rows.to_sql(table_name, engine, if_exists='append', index=False)
        logger.info(f"Data loaded into PostgreSQL table '{table_name}' ({len(new_rows)} new rows)")
        return len(new_rows)
    else:
        logger.info("No new rows to insert.")
        return 0
