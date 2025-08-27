from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from app.etl.pipeline import run_etl_pipeline
from app.utils.logger import logger
from app.config import (
    SCHEDULE_TYPE, SCHEDULE_MINUTES, SCHEDULE_HOUR, SCHEDULE_MINUTE
)

def start_scheduler():
    """
    Starts a background scheduler for the ETL pipeline.
    Schedule is fully configurable via config.py / .env
    """
    executors = {"default": ThreadPoolExecutor(5)}
    scheduler = BackgroundScheduler(executors=executors)

    if SCHEDULE_TYPE == "interval":
        scheduler.add_job(
            run_etl_pipeline,
            'interval',
            minutes=SCHEDULE_MINUTES,
            id="etl_interval_job",
            max_instances=1,
            misfire_grace_time=60
        )
        logger.info(f"Scheduler started: ETL runs every {SCHEDULE_MINUTES} minutes")

    elif SCHEDULE_TYPE == "cron":
        scheduler.add_job(
            run_etl_pipeline,
            'cron',
            hour=SCHEDULE_HOUR,
            minute=SCHEDULE_MINUTE,
            id="etl_cron_job",
            max_instances=1,
            misfire_grace_time=3600
        )
        logger.info(f"Scheduler started: ETL runs daily at {SCHEDULE_HOUR}:{SCHEDULE_MINUTE:02d}")

    else:
        logger.warning("Scheduler type is invalid. No jobs scheduled.")

    scheduler.start()
    return scheduler
