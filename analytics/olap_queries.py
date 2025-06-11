# olap_queries.py
"""
Simple OLAP queries for detecting IP spikes and login anomalies.
"""
from storage.duckdb_loader import run_duckdb_query
from storage.clickhouse_loader import run_clickhouse_query
import pandas as pd

def detect_ip_spikes_duckdb(table_name: str, db_path: str = './storage/logs.duckdb', threshold: int = 100):
    query = f"""
        SELECT source_ip, COUNT(*) as event_count
        FROM {table_name}
        GROUP BY source_ip
        HAVING event_count > {threshold}
        ORDER BY event_count DESC
    """
    return run_duckdb_query(query, db_path)

def detect_login_anomalies_duckdb(table_name: str, db_path: str = './storage/logs.duckdb', threshold: int = 10):
    query = f"""
        SELECT user, COUNT(*) as login_count
        FROM {table_name}
        WHERE event_type = 'login'
        GROUP BY user
        HAVING login_count > {threshold}
        ORDER BY login_count DESC
    """
    return run_duckdb_query(query, db_path)

def detect_ip_spikes_clickhouse(table_name: str, threshold: int = 100):
    query = f"""
        SELECT source_ip, COUNT(*) as event_count
        FROM {table_name}
        GROUP BY source_ip
        HAVING event_count > {threshold}
        ORDER BY event_count DESC
    """
    return run_clickhouse_query(query)

def detect_login_anomalies_clickhouse(table_name: str, threshold: int = 10):
    query = f"""
        SELECT user, COUNT(*) as login_count
        FROM {table_name}
        WHERE event_type = 'login'
        GROUP BY user
        HAVING login_count > {threshold}
        ORDER BY login_count DESC
    """
    return run_clickhouse_query(query)
