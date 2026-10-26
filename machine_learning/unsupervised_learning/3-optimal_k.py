#!/usr/bin/env python3
"""Task 3"""
from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    """evaluates K-Means clustering quality
    using silhouette scores to measure cluster cohesion and separation,
    and to compute the inertia to be used for the elbow method
    """
    cluster_numbers = []
    inertia_values = []
    silhouette_scores = []
    for i in range(2, max_clusters+1):
        k_means_model = K_Means(X, i, random_state)
        cluster_numbers.append(i)
        inertia_values.append(k_means_model.inertia_)
        score = metrics.silhouette_score(X, k_means_model.labels_)
        silhouette_scores.append(score)
    
    return cluster_numbers, inertia_values, silhouette_scores
    
