#!/usr/bin/env python3
"""module 0"""
from tensorflow import keras


def build_model(input_dim, neuros_h):
    """creates a shallow neural network with a single hidden layer"""
    model = keras.sequential([
        keras.layers.Input(shape=(input_dim,)),
        keras.layers.Dense(neurons_h, activation='sigmoid'),
        keras.layers.Dense(3, activation='softmax')
    ])

    return model  
