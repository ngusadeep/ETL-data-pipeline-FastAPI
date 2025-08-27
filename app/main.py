from fastapi import FastAPI, HTTPException
from pathlib import Path
from app.db.db import get_postgres_engine
from app.etl.extract import extract_data
from app.etl.transform import transform_data
from app.etl.load import load_data_to_db

app = FastAPI(title="ETL Pipeline API")

# --- Paths & table ---
RAW_FILE = Path(__file__).parent.parent / "data/raw/sales_data.csv"
TABLE_NAME = "sales_table"

# --- Routes ---
@app.get('/')
def root():
    return {'message': 'ETL Pipeline API is running!'}

@app.post('/run-etl')
def run_etl():
    try:
        # --- Extract ---
        if not RAW_FILE.is_file():
            raise FileNotFoundError(f"CSV file not found at {RAW_FILE.resolve()}")
        raw_data = extract_data(RAW_FILE)

        # --- Transform ---
        transformed_data = transform_data(raw_data)

        # --- Load ---
        engine = get_postgres_engine()
        load_data_to_db(transformed_data, TABLE_NAME, engine)

        return {'status': 'success', 'message': f'Data added successfully into table {TABLE_NAME}'}

    except FileNotFoundError as fnf_err:
        raise HTTPException(status_code=404, detail=str(fnf_err))

    except ValueError as val_err:
        raise HTTPException(status_code=400, detail=str(val_err))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
