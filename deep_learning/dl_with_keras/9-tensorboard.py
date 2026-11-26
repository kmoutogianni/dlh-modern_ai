#!/usr/bin/env python3
"""module 9"""
from tensorflow import keras
import datetime


def log_to_tensorboard(log_dir, model, X, Y, epochs, verbose=1):
    """logs a Keras model’s training metrics to TensorBoard"""
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = log_dir + "/" + timestamp

    tensorboard = keras.callbacks.TensorBoard(
        log_dir=log_dir,
        histogram_freq=1
    )

    model.fit(
        X,
        Y,
        epochs=epochs,
        callbacks=[tensorboard],
        verbose=verbose
    )
