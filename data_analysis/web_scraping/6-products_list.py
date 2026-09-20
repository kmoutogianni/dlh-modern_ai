#!/usr/bin/env python3
import time
from selenium import webdriver

def scrape_products(url):
    """ Opens a static product category page in headless Chrome and returns a list of dictionaries with keys: 'title', 'price', 'description', 'rating'. """

    # create the options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    # create the driver
    driver = webdriver.Chrome(options=options)
    products = []
    
    driver.get(url)
    time.sleep(1)
    
    product_elements = driver.find_elements(
        webdriver.common.by.By.CSS_SELECTOR,
        "div.thumbnail"
    )
    for elem in product_elements:
        title_elem = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "a"
        )
        title = title_elem.get_attribute("title")

        price_elem = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "h4.price"
        )
        price = price_elem.text.strip()

        desc_elem = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            "p.description"
        )
        description = desc_elem.text.strip()

        rating_elem = elem.find_element(
            webdriver.common.by.By.CSS_SELECTOR,
            ".ratings p[data-rating]"
        )
        rating = int(rating_elem.get_attribute("data-rating"))

        products.append({
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        })
  
      driver.quit()
      return products
