#!/usr/bin/env python3
"""module 7"""
import tensorflow as tf


def predict(model, X, verbose=0):
    """makes predictions on a given dataset using a trained Keras model"""

    predictions = model.predict(X, verbose=verbose)
    return predictions
