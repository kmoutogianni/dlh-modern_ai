#!/usr/bin/env python3
"""module 6"""
from tensorflow import keras


def save_model_weights(model, filepath):
    """saves only the weights of a trained Keras model"""
    model.save_weights(filepath)


def load_model_weights(model, filepath):
    """re-loads only the weights of a trained Keras model"""
    model.load_weights(filepath)
