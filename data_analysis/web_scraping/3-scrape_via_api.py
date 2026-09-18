#!/usr/bin/env python3
"""Module 3"""
import json 
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """fetches quote data from all the quotes' API pages"""
    page_no = 1
    url = f"{base_url}/api/quotes?page={page_no}"
    result = []
    while True:
        response = fetch_html(url)
        quotes = response.json()
        if not quotes:
            break
        quote_dict = {
            "text": quotes["text"],
            "author": quotes["author"],
            "tags": quotes["tags"]
        }
        result.append(quote_dict)
    return result
