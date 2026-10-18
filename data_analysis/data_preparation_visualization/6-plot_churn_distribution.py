#!/usr/bin/env python3
"""Task 5"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """visualizes churn class distribution"""
    plt.figure(figsize=(12, 8))
    plt.ylabel('Count')
    plt.xlabel('')
    plt.title('Churn Distribution')
    df['Churn'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'], rot=0)
    plt.show()
