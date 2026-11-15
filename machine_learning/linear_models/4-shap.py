#!/usr/bin/env python3
"""module 4"""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """helps generate model explanations using the SHAP library"""

    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
