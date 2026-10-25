#!/usr/bin/env python3
"""Task 0"""
from sklearn import preprocessing


def Standardize(X):
    """standardizes tabular data using Scikit-learn"""
scaler = preprocessing.StandardScaler()
standardized_array = scaler.fit_transform(X)
return standardized_array
