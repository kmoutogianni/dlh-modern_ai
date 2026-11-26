#!/usr/bin/env python3
"""module 8"""
from tensorflow import keras


def build_deep_model(input_dim, hidden_layers):
    """creates a deep neural network"""
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(input_dim,)))
    for neurons in hidden_layers:
        model.add(keras.layers.Dense(neurons, activation='relu'))
    return model
