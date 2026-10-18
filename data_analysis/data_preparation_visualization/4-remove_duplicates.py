#!/usr/bin/env python3
"""task 4"""


def remove_duplicates(df):
    """Remove duplicate rows from a DataFrame."""
    return df.drop_duplicates()
