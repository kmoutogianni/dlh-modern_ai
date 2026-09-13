#!/usr/bin/env python3
"""Module 1"""

from bs4 import BeautifulSoup 
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
  """scrapes the first page of quotes from quotes.toscrape.com"""
  html_page = fetch_html(url)
  soup = BeautifulSoup(html_page)
  
  quote_block = soup.find_all('div', class_='quote')
  quotes = []

  for quote in quote_block:
    text = quote.find('span', class_='text').text.strip()
    author = quote.find('small', class_='author').text.strip()
    tag_list = quote.find_all('a', class_='tag')
    tags = []
    for tag in tag_list:
        tags.append(tag.text.strip())
    quotes.append({'text' : text, 'author' : author, 'tags' : tags}) 
  return quotes
