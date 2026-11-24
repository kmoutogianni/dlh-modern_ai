#!/usr/bin/env python3
"""module 3"""


def train_model(model, X, Y, epochs, verbose=1):
    """trains a Keras model"""
    model.fit(X, Y, epochs=epochs, verbose=verbose)
