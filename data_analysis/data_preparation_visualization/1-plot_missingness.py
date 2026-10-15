#!/usr/bin/env python3
"""task 1"""
import numpy as np
import matplotlib.pyplot as plt


def plot_missingness(df):
    """visualizes missing values"""
    missing = df.isnull()

    for i, column in enumerate(df.columns):
        plt.scatter(
            df.index[missing[column]],
            [i] * missing[column].sum(),
            marker='|'
        )

    plt.yticks(range(len(df.columns)), df.columns)
    plt.show()
