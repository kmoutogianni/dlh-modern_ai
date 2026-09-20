#!/usr/bin/env python3
"""Module for extracting quotes from JSON-LD."""

import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quotes from JSON-LD embedded in a webpage."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    result = []

    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        data = json.loads(script.string)

        if data.get("@type") == "Quote":
            text = data.get("text")
            author = data.get("author", {}).get("name")
            tags = data.get("keywords", [])

            if isinstance(tags, str):
                tags = [tag.strip() for tag in tags.split(",")]

            result.append({
                "text": text,
                "author": author,
                "tags": tags
            })

    return result
