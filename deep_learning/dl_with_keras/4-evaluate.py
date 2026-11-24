#!/usr/bin/env python3
"""module 4"""


def evaluate_model(model, X, Y, verbose=0):
    """assesses a trained Keras model's performance"""
    loss, accuracy = model.evaluate(X, Y, verbose=verbose)
    return loss, accuracy
