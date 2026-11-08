#!/usr/bin/env python3
"""Task 4"""
from sklearn import cluster
from sklearn import metrics
Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(
        X, n_clusters, random_state, n_components,
        use_pca_data=True):
    """performs Agglomerative hierarchical clustering"""

    if use_pca_data is True:
        X_used, pca_model = Apply_PCA(
            X, n_components, random_state
        )
    else:
        X_used = X

    model = cluster.AgglomerativeClustering(
        n_clusters=n_clusters,
        linkage="ward"
    )
    model.fit(X_used)

    if n_clusters > 1:
        silhouette = metrics.silhouette_score(
            X_used, model.labels_
        )
    else:
        silhouette = None

    return model, X_used, silhouette
