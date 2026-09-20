#!/usr/bin/env python3
"""Module 8"""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=0.5):
    """Scrolls through an infinite-scroll page and extracts all products."""

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    last_height = driver.execute_script(
        "return document.body.scrollHeight"
    )

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(scroll_pause)

        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        if new_height == last_height:
            break

        last_height = new_height

    product_elements = driver.find_elements(
        webdriver.common.by.By.CSS_SELECTOR,
        "div.thumbnail"
    )

    products = []
    seen = set()

    for elem in product_elements:
        title_elem = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "a.title"
        )
        title = title_elem.get_attribute("title")

        price = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "h4.price"
        ).text.strip()

        description = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "p.description"
        ).text.strip()

        ratings = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            ".ratings"
        )

        stars = ratings.find_elements(
            webdriver.common.by.By.CSS_SELECTOR,
            "span.ws-icon.ws-icon-star"
        )

        rating = len(stars)

        product_key = (title, price)

        if product_key in seen:
            continue

        seen.add(product_key)

        products.append({
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        })

    driver.quit()

    return products
