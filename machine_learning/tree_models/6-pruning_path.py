#!/usr/bin/env python3
"""module 6"""


def get_pruning_path(clf, X, y):
    """retrieves the cost-complexity pruning path
    for a given decision tree classifier"""

    path = clf.cost_complexity_pruning_path(X, y)

    ccp_alphas = path.ccp_alphas
    impurities = path.impurities

    return ccp_alphas, impurities
