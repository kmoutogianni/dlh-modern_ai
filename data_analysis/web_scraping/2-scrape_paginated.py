#!/usr/bin/env python3
"""Module 2"""

from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def def scrape_paginated(base_url):
    """follows “Next” links until no more pages remain"""
