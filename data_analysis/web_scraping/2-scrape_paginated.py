#!/usr/bin/env python3
"""Module 2"""

from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def def scrape_paginated(base_url):
    """follows “Next” links until no more pages remain"""
