from app.etl.extract import extract_data
from app.etl.transform import transform_data
from app.etl.load import load_data_to_db
from app.db.db import get_postgres_engine
from app.utils.logger import logger
from app.config import RAW_FILE_PATH, TABLE_NAME

def run_etl_pipeline() -> dict:
    """
    Runs the full ETL pipeline: extract → transform → load.
    Returns information about the load (number of new rows inserted).
    """
    try:
        logger.info("ETL pipeline started")

        # --- Extract ---
        if not RAW_FILE_PATH.is_file():
            raise FileNotFoundError(f"CSV file not found at {RAW_FILE_PATH.resolve()}")
        data = extract_data(RAW_FILE_PATH)

        # --- Transform ---
        transformed_data = transform_data(data)

        # --- Load ---
        engine = get_postgres_engine()
        rows_loaded = load_data_to_db(transformed_data, TABLE_NAME, engine)

        logger.info(f"ETL pipeline completed successfully, {rows_loaded} new rows loaded to {TABLE_NAME}")

        return {"rows_loaded": rows_loaded}

    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}", exc_info=True)
        raise
