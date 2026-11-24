#!/usr/bin/env python3
"""module 5"""
from tensorflow import keras


def save_model(model, filepath):
    """save a Keras model"""
    model.save(filepath=filepath)


def load_model(filepath):
    """loads a saved Keras model"""
    keras.models.load_model(filepath)
