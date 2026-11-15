#!/usr/bin/env python3
"""module 0"""
from sklearn import linear_model


def Linear_Regression():
    """creates a linear regression model
    which uses ordinary least squares
    to fit a linear model to the data"""

    model = linear_model.LinearRegression()
    return model
