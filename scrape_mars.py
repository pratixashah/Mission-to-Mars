
 
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

    time.sleep(1)

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

# Mars Facts
def mars_facts(Browser):
    mars_fact_url = "https://space-facts.com/mars/"

    table = pd.read_html(mars_fact_url)
    df_mars_facts = table[0]

    # print(df_mars_facts)

    df_mars_facts.columns=["Description", "Mars"]
    df_mars_facts = df_mars_facts.set_index(["Description"])

    print(df_mars_facts)

    df_mars_facts.to_html('mars_facts_table1.html')

    return df_mars_facts

mars_news(Browser)
mars_featured_image(Browser)
mars_facts(Browser)


