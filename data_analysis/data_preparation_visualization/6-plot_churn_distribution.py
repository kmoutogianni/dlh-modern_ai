#!/usr/bin/env python3
"""task 5"""


def plot_churn_distribution(df):
    df['Churn'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
