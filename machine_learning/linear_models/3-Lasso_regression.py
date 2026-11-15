#!/usr/bin/env python3
"""module 3"""
from sklearn import linear_model


def lasso_regression(random_state):
    """creates and returns a Lasso Regression model"""
    model = linear_model.Lasso(random_state=random_state)
    return model
