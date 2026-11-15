#!/usr/bin/env python3
"""module 10"""
import numpy as np


def feature_importance(rf):
    """computes and returns the feature importances 
    from a trained random forest model"""

    importances = rf.feature_importances_
    indices= np.argsort(importances)
      
