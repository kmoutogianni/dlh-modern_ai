#!/usr/bin/env python3
"""module 4"""
from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """generates a detailed classification report"""
    return metrics.classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names
    )
