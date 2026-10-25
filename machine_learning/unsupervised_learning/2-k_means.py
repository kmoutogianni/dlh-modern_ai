#!/usr/bin/env python3
"""Task 1"""
from sklearn import cluster


def K_Means(X, n_clusters, random_state):
    """creates and fits a K-Means clustering model 
    using Scikit-learn on tabular data"""
    k_means_model = cluster.KMeans(
        n_clusters=n_clusters, random_state=random_state
    )
    fitted_model = k_means_model.fit(X)
    return fitted_model
