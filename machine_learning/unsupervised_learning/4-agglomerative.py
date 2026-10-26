#!/usr/bin/env python3
"""Task 4"""
from sklearn import cluster
from sklearn import metrics
Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(X, n_clusters, random_state, n_components, use_pca_data=True)
    """performs Agglomerative hierarchical clustering on tabular data using Scikit-learn"""
