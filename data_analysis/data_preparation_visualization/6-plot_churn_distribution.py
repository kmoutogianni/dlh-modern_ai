#!/usr/bin/env python3
"""task 5"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """visualizes churn class distribution"""
    df['Churn'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
