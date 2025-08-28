import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.etl.pipeline import run_etl_pipeline

if __name__ == "__main__":
    result = run_etl_pipeline()
    print(result)
