#!/usr/bin/env python3
"""Task 14"""
import pandas as pd


def create_features(df):
    """Creates new features from the dataset."""
    df = df.copy()

    service_columns = [
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies'
    ]

    # Count subscribed services, including internet service
    df['NumServices'] = (
        df[service_columns].eq('Yes').sum(axis=1)
        + df['InternetService'].isin(['DSL', 'Fiber optic']).astype(int)
    )

    # Group customers by tenure
    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'],
        right=True
    )

    # Drop original columns used and PhoneService
    columns_to_drop = service_columns + [
        'InternetService', 'tenure'
    ]
    df = df.drop(columns=columns_to_drop)


    return df
