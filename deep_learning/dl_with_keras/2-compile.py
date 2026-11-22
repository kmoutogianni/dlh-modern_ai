#!/usr/bin/env python3
"""module 2"""
from tensorflow import keras


def compile_model(model, learning_rate=0.01):
    """configures the keras model for training"""

    optimizer = keras.optimizers.SGD(
        learning_rate=learning_rate
    )

    model.compile(
        optimizer=optimizer,
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
