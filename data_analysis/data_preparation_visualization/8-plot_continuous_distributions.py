#!/usr/bin/env python3
"""Task 8"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Visualizes continuous numerical feature distributions."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include='number').columns

    n = len(columns_to_plot)
    fig, axes = plt.subplots(n, 2, figsize=(15, 5 * n))

    if n == 1:
        axes = np.array([axes])

    for i, column in enumerate(columns_to_plot):
        data = df[column].dropna()

        axes[i, 0].hist(
            data,
            bins=30,
            density=True,
            alpha=0.7,
            edgecolor='black'
        )

        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 100)
        axes[i, 0].plot(x, kde(x), color='red')

        axes[i, 0].set_title(f'{column} Histogram + KDE')
        axes[i, 0].set_ylabel('')

        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(f'{column} Boxplot')
        axes[i, 1].set_ylabel('')
        axes[i, 1].set_yticks([])

    plt.tight_layout()
    plt.show()
    return None
