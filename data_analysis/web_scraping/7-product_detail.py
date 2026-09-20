#!/usr/bin/env python3
"""Module 7"""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Scrapes the details of one product."""

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(delay)

    caption_h4s = driver.find_elements_by_css_selector(".caption h4")
    title = caption_h4s[1].text.strip() if len(caption_h4s) > 1 else ""
    price_elem = driver.find_element_by_css_selector("h4.price")
    price = price_elem.text.strip()
    desc_elem = driver.find_element_by_css_selector("p.description")
    description = desc_elem.text.strip()
    stars = driver.find_elements_by_css_selector(".ratings p.ws-icon.ws-icon-star")
    rating = len(stars)

    driver.quit()

    return {
        "title": title,
        "price": price,
        "description": description,
        "rating": rating
    }
