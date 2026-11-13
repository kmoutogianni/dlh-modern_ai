#!/usr/bin/env python3
"""module 5"""
from sklearn import model_selection


def prepruning(X, y, clf):
    """performs a Grid Search for the best pre-pruning hyperparameters
    for a decision tree classifier"""
    param_grid = {
        'criterion': ['gini', 'entropy'],
        'max_depth': list(range(2, 5)),
        'min_samples_leaf': list(range(2, 5)),
        'min_samples_split': list(range(2, 5))
    }

    grid_search = model_selection.GridSearchCV(clf, param_grid)
    grid_search.fit(X, y)

    return grid_search.best_params_
