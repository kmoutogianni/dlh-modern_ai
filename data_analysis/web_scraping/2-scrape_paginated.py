#!/usr/bin/env python3
"""Module 2"""

from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """follows “Next” links until no more pages remain"""
    quotes = []
    current_url = base_url

    while current_url:
        html = fetch_html(current_url)
        quotes.extend(scrape_basic(current_url))

        soup = BeautifulSoup(html, "html.parser")
        next_link = soup.select_one("li.next a")

        if not next_link:
            break

        next_href = next_link.get("href")
        current_url = parse.urljoin(current_url, next_href)

        time.sleep(1)

    return quotes
