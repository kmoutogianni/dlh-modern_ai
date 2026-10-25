#!/usr/bin/env python3
"""Task 1"""
from sklearn import decomposition


def Apply_PCA(X, n_components, random_state):
    """performs Principal Component Analysis (PCA)
    on tabular data using Scikit-learn"""
    pca_function = decomposition.PCA(
        n_components=n_components,
        random_state=random_state
    )
    X_transformed = pca_function.fit_transform(X)
    return X_transformed, pca_function
