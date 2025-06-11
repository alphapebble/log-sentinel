# sysmon_parser.py
"""
Parser for Sysmon Windows Event logs (CSV or JSON).
Outputs: pandas.DataFrame with normalized columns.
"""
import pandas as pd
import json

def parse_sysmon_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    if 'utc_time' in df.columns:
        df['utc_time'] = pd.to_datetime(df['utc_time'], errors='coerce')
    return df

def parse_sysmon_json(file_path: str) -> pd.DataFrame:
    with open(file_path) as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    if 'utc_time' in df.columns:
        df['utc_time'] = pd.to_datetime(df['utc_time'], errors='coerce')
    return df
