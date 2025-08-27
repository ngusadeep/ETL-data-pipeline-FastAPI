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

    with engine.connect() as conn:
        try:
            existing = pd.read_sql(text(f'SELECT * FROM {table_name}'), conn)
            if not existing.empty:
                existing.columns = [col.lower() for col in existing.columns]
                # Use specific columns for identifying duplicates
                merge_cols = ['sales_amount', 'unit_price', 'unit_cost']
                merged = pd.merge(df, existing, on=merge_cols, how='left', indicator=True)
                new_rows = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])
            else:
                new_rows = df
        except Exception as e:
            # Handle case where table doesn't exist yet
            if "does not exist" in str(e):
                logger.info(f"Table '{table_name}' does not exist. Creating it.")
                new_rows = df
            else:
                raise e

    # Insert only new rows
    if not new_rows.empty:
        new_rows.to_sql(table_name, engine, if_exists='append', index=False)
        logger.info(f"Data loaded into PostgreSQL table '{table_name}' ({len(new_rows)} new rows)")
        return len(new_rows)
    else:
        logger.info("No new rows to insert.")
        return 0
