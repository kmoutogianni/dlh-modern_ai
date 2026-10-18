#!/usr/bin/env python3
"""Task 15"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encodes categorical features for modeling."""
    df = df.copy()

    # Encode Churn
    label_encoder = preprocessing.LabelEncoder()
    df['Churn'] = label_encoder.fit_transform(df['Churn'])

    # Encode binary columns
    binary_columns = [
        'Partner', 'Dependents', 'PaperlessBilling', 'SeniorCitizen'
    ]
    ordinal_encoder = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']] * len(binary_columns)
    )
    df[binary_columns] = ordinal_encoder.fit_transform(df[binary_columns])

    # One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True,
        dtype=int
    )

    # Encode TenureGroup in alphabetical order
    tenure_encoder = preprocessing.OrdinalEncoder()
    df[['TenureGroup']] = tenure_encoder.fit_transform(df[['TenureGroup']])

    return df, label_encoder, ordinal_encoder, tenure_encoder
