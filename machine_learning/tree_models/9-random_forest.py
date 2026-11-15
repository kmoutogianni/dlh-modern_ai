#!/usr/bin/env python3
"""module 9"""
from sklearn import ensemble


def random_forest(n_estimators, random_state):
"""creates a random forest classifier"""
    model = ensemble.RandomForestClassifier(
        n_estimators=n_estimators, random_state
    )
    return model
