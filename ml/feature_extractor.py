# feature_extractor.py
"""
Feature extraction for time- and user-based features from log DataFrames.
"""
import pandas as pd

def extract_time_user_features(df: pd.DataFrame, time_col: str = 'timestamp', user_col: str = 'user') -> pd.DataFrame:
    df = df.copy()
    # Ensure datetime
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    df = df.sort_values(time_col)
    # Time since last event (per user)
    df['time_since_last_event'] = df.groupby(user_col)[time_col].diff().dt.total_seconds().fillna(0)
    # Event count per user
    user_event_counts = df.groupby(user_col)[time_col].transform('count')
    df['user_event_count'] = user_event_counts
    # Hour of day
    df['hour'] = df[time_col].dt.hour
    # Day of week
    df['dayofweek'] = df[time_col].dt.dayofweek
    return df
