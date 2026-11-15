#!/usr/bin/env python3
"""module 0"""
from tensorflow import keras


def build_model(input_dim, neurons_h):
    """Build a shallow neural network"""

    model = keras.Sequential([
        keras.layers.Dense(neurons_h, activation='sigmoid',
                           input_shape=(input_dim,)),
        keras.layers.Dense(10, activation='softmax')
    ])

    return model
