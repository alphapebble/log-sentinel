# xgb_anomaly.py
"""
Train and apply XGBoost model for anomaly classification on extracted features.
"""
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_xgb_classifier(df: pd.DataFrame, label_col: str, feature_cols: list, test_size: float = 0.2, random_state: int = 42):
    X = df[feature_cols]
    y = df[label_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    report = classification_report(y_test, y_pred, output_dict=True)
    return model, report, X_test, y_test, y_pred, y_prob

def predict_anomaly(model, df: pd.DataFrame, feature_cols: list, threshold: float = 0.5):
    proba = model.predict_proba(df[feature_cols])[:, 1]
    flag = (proba > threshold).astype(int)
    return flag, proba
