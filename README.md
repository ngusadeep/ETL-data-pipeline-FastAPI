# FastAPI ETL Pipeline

A cloud-ready ETL pipeline built with **FastAPI** that extracts CSV data, transforms it, and loads it into a **PostgreSQL database**. Fully containerized with Docker and compatible with **Neon Postgres**.


## Features

- Extract data from CSV files
<<<<<<< HEAD
- Transform and clean data using Pandas
- Load data into PostgreSQL (Neon-compatible)
=======
- Transform and clean data
- Load data into PostgreSQL tables for every 3 minutes
>>>>>>> 40a4403d9ffca68d54673be495c4a1d56a90c533
- REST API endpoints:
  - `/` → Health check
  - `/run-etl` → Trigger the ETL pipeline
- Docker-ready
- Environment-based configuration via `.env`
- Optional scheduling (interval or cron) for automated ETL runs


## Tech Stack

- Python 3.12+
- FastAPI
- Pandas
- SQLAlchemy / psycopg2-binary
- PostgreSQL (Neon-compatible)
- Docker
- APScheduler (for scheduling)


## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-etl-pipeline.git
cd fastapi-etl-pipeline
```

### 2. Create `.env` file
Create a `.env` file in the project root (or copy from `.env.example`):

```env
# Database
DATABASE_URL=postgresql://<your-username>:<your password>@ep-broad-cell-adat0ldo-pooler.c-2.us-east-1.aws.neon.tech/<your_db_name>?sslmode=require&channel_binding=require

# FastAPI
PORT=8000

# ETL
RAW_FILE_PATH=data/raw/sales_data.csv
TABLE_NAME=sales_table

# Scheduler
SCHEDULE_TYPE=interval        # options: interval or cron
SCHEDULE_MINUTES=3            # used if SCHEDULE_TYPE=interval
SCHEDULE_HOUR=2               # used if SCHEDULE_TYPE=cron
SCHEDULE_MINUTE=0             # used if SCHEDULE_TYPE=cron
```

### 3. Build Docker Image
```bash
docker build -t fastapi-etl .
```

### 4. Run the container
```bash
docker run --env-file .env -p 8000:8000 fastapi-etl
```

### 5. Access the API
- Health check → [http://localhost:8000/](http://localhost:8000/)  
- Run ETL (POST) → [http://localhost:8000/run-etl](http://localhost:8000/run-etl)


## Directory Structure

```
fastapi-etl-pipeline/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entrypoint
│   ├── etl/
│   │   ├── __init__.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   └── db/
│       └── db.py
├── data/
│   └── raw/
│       └── sales_data.csv
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── .env.example
```


## Notes

- Ensure `pandas` and `psycopg2-binary` versions are compatible with Python 3.12.
- `DATABASE_URL` should include SSL options for Neon Postgres (already included above).
- Scheduler can be configured via `.env`:
  - **Interval mode** → runs ETL every *N minutes*  
  - **Cron mode** → runs ETL at a specific hour/minute daily  
- ETL logs will appear in the container console.


## License

MIT License
````