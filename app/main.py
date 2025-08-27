from fastapi import FastAPI, HTTPException
from app.etl.pipeline import run_etl_pipeline
from app.scheduler import start_scheduler
from app.utils.logger import logger

app = FastAPI(title="ETL Pipeline API")

# --------------------------
# Scheduler
# --------------------------
scheduler = None

@app.on_event("startup")
def startup_event():
    """Start the background scheduler when FastAPI starts."""
    global scheduler
    scheduler = start_scheduler()
    logger.info("Scheduler initialized on startup.")

# --------------------------
# Routes
# --------------------------
@app.get("/")
def root():
    """Health check / root endpoint."""
    return {"message": "ETL Pipeline API is running!"}


@app.post("/run-etl")
def trigger_etl():
    """
    Manual ETL trigger via API.
    Runs the full ETL pipeline (extract → transform → load)
    """
    try:
        # Run ETL and optionally return number of rows loaded
        result = run_etl_pipeline()
        return {
            "status": "success",
            "message": "ETL run completed successfully",
            "rows_loaded": result.get("rows_loaded", None)
        }

    except FileNotFoundError as fnf_err:
        logger.error(f"ETL failed: {fnf_err}", exc_info=True)
        raise HTTPException(status_code=404, detail=str(fnf_err))

    except ValueError as val_err:
        logger.error(f"ETL failed: {val_err}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(val_err))

    except Exception as e:
        logger.error(f"ETL failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
