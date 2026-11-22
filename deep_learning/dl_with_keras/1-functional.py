#!/usr/bin/env python3
"""module 1"""
from tensorflow import keras


def build_model(input_dim, neurons_h):
    """create a shallow neural network with a single hidden layer
    to perform multi-class classification,
    without using the Sequential class"""

    inputs = keras.Input(shape=(input_dim,))

    hidden = keras.layers.Dense(
        neurons_h, activation='sigmoid'
    )(inputs)

    outputs = keras.layers.Dense(
        10, activation='softmax'
    )(hidden)

    model = keras.Model(inputs=inputs, outputs=outputs)
    return model
