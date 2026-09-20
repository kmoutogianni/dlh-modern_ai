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

    caption = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR,
        ".caption"
    )

    h4_elements = caption.find_elements(
        webdriver.common.by.By.CSS_SELECTOR,
        "h4"
    )
    title = h4_elements[1].text.strip()

    price = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR,
        "h4.price"
    ).text.strip()

    description = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR,
        "p.description"
    ).text.strip()

    ratings = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR,
        ".ratings"
    )

    print(ratings.get_attribute("innerHTML"))

    stars = ratings.find_elements(
        webdriver.common.by.By.CSS_SELECTOR,
        "p.ws-icon.ws-icon-star"
    )
    rating = len(stars)

    driver.quit()

    return {
        "title": title,
        "price": price,
        "description": description,
        "rating": rating
    }
