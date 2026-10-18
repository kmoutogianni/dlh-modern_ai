#!/usr/bin/env python3
"""Task 7"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Visualizes categorical feature distributions."""
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.select_dtypes(include='object').columns
            if col != 'Churn'
        ]
    else:
        columns_to_plot = columns_to_plot

    n_cols = 3
    n_rows = 6

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    for i, column in enumerate(columns_to_plot):
        df[column].value_counts().plot(
            kind='bar',
            ax=axes[i],
            rot=45
        )
        axes[i].set_title(column)
        axes[i].set_xlabel('')

    for i in range(len(columns_to_plot), len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
