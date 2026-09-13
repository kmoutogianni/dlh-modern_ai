#!/usr/bin/env python3
"""Module 0"""

import requests


def fetch_html(url, headers=None, timeout=10):
    """fetches a web page and returns its HTML as text"""
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
