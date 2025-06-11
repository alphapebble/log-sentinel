# sessionizer.py
"""
Sessionize logs into windows of N lines (default 10).
"""
import pandas as pd
from typing import List

def sessionize_logs(df: pd.DataFrame, window_size: int = 10) -> List[List[str]]:
    sessions = []
    for i in range(0, len(df), window_size):
        session = df.iloc[i:i+window_size].astype(str).agg(' | '.join, axis=1).tolist()
        sessions.append(session)
    return sessions
