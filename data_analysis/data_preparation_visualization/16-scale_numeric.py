#!/usr/bin/env python3
"""Module 15"""
import pandas as pd
from sklearn import preprocessing


def scale_numeric(df):
    """standardizes numeric columns"""
    columns = ['MonthlyCharges', 'TotalCharges']

    scaler = preprocessing.StandardScaler()

    df[columns] = scaler.fit_transform(df[columns])

    return df
