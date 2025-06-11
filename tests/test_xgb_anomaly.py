# test_xgb_anomaly.py
"""
Test script for feature extraction and XGBoost anomaly classification.
"""
import pandas as pd
from ml.feature_extractor import extract_time_user_features
from ml.xgb_anomaly import train_xgb_classifier, predict_anomaly

def main():
    # Example synthetic data
    data = {
        'timestamp': pd.date_range('2023-01-01', periods=100, freq='H'),
        'user': ['user1']*50 + ['user2']*50,
        'event_type': ['login']*100,
        'is_anomaly': [0]*90 + [1]*10
    }
    df = pd.DataFrame(data)
    df = extract_time_user_features(df, time_col='timestamp', user_col='user')
    feature_cols = ['time_since_last_event', 'user_event_count', 'hour', 'dayofweek']
    model, report, X_test, y_test, y_pred, y_prob = train_xgb_classifier(df, label_col='is_anomaly', feature_cols=feature_cols)
    print('Classification report:', report)
    # Predict on all data
    flag, prob = predict_anomaly(model, df, feature_cols)
    print('Binary flag:', flag)
    print('Confidence score:', prob)

if __name__ == '__main__':
    main()
