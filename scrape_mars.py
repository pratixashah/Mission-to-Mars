
 
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import bs4 
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd

# NASA Mars Top News
def mars_news(Browser):
    mars_news_url = "https://mars.nasa.gov/news"

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(mars_news_url)

    # response = requests.get(space_image_url, verify=False)

    html = browser.html
    soup = bs(html, 'html.parser')
    # print(soup.prettify())

    time.sleep(2)

    news_title = soup.select_one("div.content_title a").text
    print(news_title)

    news_text = soup.select_one("div.article_teaser_body").text
    print(news_text)

    browser.quit()

    return news_title,news_text


mars_news(Browser)
