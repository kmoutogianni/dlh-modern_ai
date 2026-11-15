#!/usr/bin/env python3
"""module 1"""
from sklearn import linear_model


def ridge_regression(random_state):
    """creates and returns a Ridge Regression model"""
    model = linear_model.Ridge(random_state=random_state)
    return model
