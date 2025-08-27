from sqlalchemy.engine import Engine
import pandas as pd

def load_data_to_db(data: pd.DataFrame, table_name: str, engine: Engine):
    data.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded into PostgreSQL table '{table_name}'")
