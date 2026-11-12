#!/usr/bin/env python3
"""module 2"""
from sklearn import tree


def draw(clf, feature_names, class_names):
    """displays the textual structure of a trained decision tree classifier"""
    print(tree.export_text(
        clf,
        feature_names=feature_names,
        class_names=class_names
    ))
