#!/usr/bin/env python3
"""task 1"""
import numpy as np
import matplotlib.pyplot as plt


def plot_missingness(df):
    """visualizes missing values"""
    for i, column in enumerate(df.columns):
        rows = df.index[df[column].isnull()]
        plt.scatter(rows, [i] * len(rows), marker='|')

    plt.yticks(range(len(df.columns)), df.columns)
    plt.title("Missingness plot")
    plt.show()
