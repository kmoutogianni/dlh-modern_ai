#!/usr/bin/env python3
import json 
import fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    page_no = 1
    url = f"{base_url}/api/quotes?page={page_no}"
    fetch_html
