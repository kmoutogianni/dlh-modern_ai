#!/usr/bin/env python3
"""module 5"""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """creates and returns a Logistic Regression model"""
    model = linear_model.LogisticRegression(
        random_state=random_state
    )
    return model
