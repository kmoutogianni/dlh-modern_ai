#!/usr/bin/env python3
"""task 5"""


def drop_customerID(df): 
    """removes the customerID column"""
    return df.drop(columns=['customerID'])
