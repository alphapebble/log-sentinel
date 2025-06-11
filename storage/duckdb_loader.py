# duckdb_loader.py
"""
Utility to load DataFrames into DuckDB and run OLAP queries.
"""
import duckdb
import pandas as pd
from typing import Optional

def load_to_duckdb(df: pd.DataFrame, table_name: str, db_path: str = './storage/logs.duckdb'):
    con = duckdb.connect(db_path)
    con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM df LIMIT 0")
    con.execute(f"INSERT INTO {table_name} SELECT * FROM df")
    con.close()

def run_duckdb_query(query: str, db_path: str = './storage/logs.duckdb') -> Optional[pd.DataFrame]:
    con = duckdb.connect(db_path)
    result = con.execute(query).fetchdf()
    con.close()
    return result
