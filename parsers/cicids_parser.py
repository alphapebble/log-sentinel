# cicids_parser.py
"""
Parser for CICIDS 2017 CSV network logs.
Outputs: pandas.DataFrame with normalized columns.
"""
import pandas as pd

def parse_cicids_csv(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    # Normalize column names
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    # Example: ensure timestamp is datetime
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    return df
