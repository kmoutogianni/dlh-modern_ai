#!/usr/bin/env python3
"""Task 3"""
from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def Agglomerative_Clustering(X, n_clusters, random_state, n_components, use_pca_data=True)
    """performs Agglomerative hierarchical clustering on tabular data using Scikit-learn"""
