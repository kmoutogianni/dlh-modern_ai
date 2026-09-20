#!/usr/bin/env python3
"""Module for logging in and scraping protected quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and scrape quotes visible after authentication."""
    session = requests.Session()

    # Get the login page
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract CSRF token
    csrf_token = soup.find("input", {"name": "csrf_token"})["value"]

    # Submit login form
    data = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }
    session.post(login_url, data=data)

    # Get protected quotes page
    response = session.get("https://quotes.toscrape.com/")
    soup = BeautifulSoup(response.text, "html.parser")

    result = []

    # Extract quotes
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        tags = []
        for tag in quote.find_all("a", class_="tag"):
            tags.append(tag.get_text(strip=True))

        result.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return result
