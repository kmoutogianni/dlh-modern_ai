#!/usr/bin/env python3
"""task 2"""
import pandas as pd


def convert_columns(df):
    """performs type conversion for specific columns"""
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
