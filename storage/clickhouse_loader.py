# clickhouse_loader.py
"""
Utility to load DataFrames into ClickHouse and run OLAP queries.
"""
import clickhouse_connect
import pandas as pd
from typing import Optional

def load_to_clickhouse(df: pd.DataFrame, table_name: str, host: str = 'localhost', port: int = 8123, user: str = 'default', password: str = ''):
    client = clickhouse_connect.get_client(host=host, port=port, username=user, password=password)
    # Create table if not exists (infer schema from DataFrame)
    columns = ', '.join([f'{col} String' for col in df.columns])
    client.command(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns}) ENGINE = MergeTree() ORDER BY tuple()")
    client.insert_df(table_name, df)

def run_clickhouse_query(query: str, host: str = 'localhost', port: int = 8123, user: str = 'default', password: str = '') -> Optional[pd.DataFrame]:
    client = clickhouse_connect.get_client(host=host, port=port, username=user, password=password)
    result = client.query_df(query)
    return result
