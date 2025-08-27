### **FastAPI ETL Pipeline

**Overview:**
A FastAPI-based ETL pipeline that extracts data from CSV files, transforms it, and loads it into a PostgreSQL database. Designed for cloud-ready deployment using Docker and compatible with Neon Postgres. Includes a REST API to trigger the ETL process and monitor the pipeline.

**Features:**

* Extract data from CSV files
* Apply transformations to clean and process data
* Load transformed data into PostgreSQL (Neon-compatible)
* REST API endpoints: `/` (health check), `/run-etl` (trigger ETL)
* Docker-ready for containerized deployments
* Environment variable configuration via `.env`

**Tech Stack:**

* Python 3.12+
* FastAPI
* Pandas
* SQLAlchemy / psycopg2-binary
* PostgreSQL (Neon-compatible)
* Docker

### **README.md**

````markdown
# FastAPI ETL Pipeline

A cloud-ready ETL pipeline built with **FastAPI** that extracts CSV data, transforms it, and loads it into a **PostgreSQL database**. The project is fully containerized with Docker and works seamlessly with **Neon Postgres**.

## Features

- Extract data from CSV files
- Transform and clean data
- Load data into PostgreSQL tables
- REST API endpoints:
  - `/` - Health check
  - `/run-etl` - Trigger the ETL pipeline
- Docker-ready
- Configurable via `.env`

## Tech Stack

- Python 3.12+
- FastAPI
- Pandas
- SQLAlchemy / psycopg2-binary
- PostgreSQL (Neon-compatible)
- Docker

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-etl-pipeline.git
cd fastapi-etl-pipeline
````

### 2. Create `.env` file

```env
DB_USERNAME=your_db_user
DB_PASSWORD=your_db_password
DB_DATABASE=your_db_name
DB_HOST=your_neon_host
DB_PORT=5432
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

* Health check: [http://localhost:8000/](http://localhost:8000/)
* Run ETL: POST request to [http://localhost:8000/run-etl](http://localhost:8000/run-etl)

### 6. Directory Structure

```
fastapi-etl-pipeline/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   └── etl/
│       ├── __init__.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       
|   └──db/
|      ├── db.py
├── data/
│   └── raw/
│       └── sales_data.csv
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Notes

* Make sure `pandas` and `psycopg2-binary` versions are compatible with Python 3.12.
* Use valid package versions in `requirements.txt` to avoid Docker build errors.
* The ETL endpoint will print logs in the container console.

## License

MIT License

```
