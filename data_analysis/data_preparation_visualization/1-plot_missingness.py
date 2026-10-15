#!/usr/bin/env python3
"""task 1"""

def plot_missingness(df):
    """visualizes missing values"""
    import matplotlib.pyplot as plt

    missing = df.isnull()

    for i, column in enumerate(df.columns):
        plt.scatter(
            df.index[missing[column]],
            [i] * missing[column].sum(),
            marker='|'
        )

    plt.yticks(range(len(df.columns)), df.columns)
    plt.xlabel('Row index')
    plt.ylabel('Column names')
    plt.show()
