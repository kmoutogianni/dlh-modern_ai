#!/usr/bin/env python3
"""module 6"""
from sklearn import svm


def get_SVM_model(name, random_state):
    """creates and returns an SVM classifier"""
    if name == 'linear':
        model = svm.SVC(kernel='linear', random_state=random_state)
    elif name == 'poly':
        model = svm.SVC(kernel='poly', random_state=random_state)
    elif name == 'rbf':
        model = svm.SVC(kernel='rbf', random_state=random_state)
    else:
        raise ValueError("Invalid kernel name")

    return model
