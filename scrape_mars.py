
 
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

# JPL Mars Space Images - Featured Image
def mars_featured_image(Browser):

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    space_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

    browser.visit(space_image_url)

    # html = browser.html
    # soup = bs(html, 'html.parser')

    time.sleep(1)

    browser.links.find_by_partial_text('FULL IMAGE').click()

    # time.sleep(1)

    html = browser.html
    soup = bs(html, 'html.parser')

    # print(soup.prettify())

    full_image_url = soup.find('img', class_="fancybox-image")

    print(full_image_url['src'])

    # print(space_image_url.split("index.html")[0])

    featured_image_url = space_image_url.split("index.html")[0] + full_image_url['src']
    print(featured_image_url)

    browser.quit()

    return featured_image_url



mars_news(Browser)
mars_featured_image(Browser)