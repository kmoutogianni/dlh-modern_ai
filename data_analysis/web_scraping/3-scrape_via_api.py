#!/usr/bin/env python3
"""Module 3"""

import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """fetches quote data from all the quotes' API pages"""
    page_no = 1
    result = []
    while True:    
        url = f"{base_url}/api/quotes?page={page_no}"
        array = json.loads(fetch_html(url))
        if not array["quotes"]:
            break
        for quote in array["quotes"]:
            quote_dict = {
                "text": quote["text"],
                "author": quote["author"]["name"],
                "tags": quote["tags"]
            }
            result.append(quote_dict)
        page_no += 1
    return result
