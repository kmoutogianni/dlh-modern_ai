#!/usr/bin/env python3
"""module 1"""
from sklearn import tree


def train_tree(clf, X, y):
    """traina a tree-based classifier"""
    clf.fit(X, y)
