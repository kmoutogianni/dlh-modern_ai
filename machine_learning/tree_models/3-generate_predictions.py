#!/usr/bin/env python3
"""module 3"""


def generate_predictions(clf, X):
    """generate predictions from a trained tree-based classifier"""
    return clf.predict(X)
