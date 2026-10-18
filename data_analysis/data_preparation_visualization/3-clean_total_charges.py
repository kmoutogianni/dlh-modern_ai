#!/usr/bin/env python3
"""task 3"""


def clean_total_charges(df, method='drop'):
    """ handles missing values in TotalCharges:
    'drop': Remove rows with missing TotalCharges
    'median': Fill with column median
    'impute': Replace with MonthlyCharges * tenure
    """
    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])

    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['TotalCharges'].median())

    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure']
        )

    return df
