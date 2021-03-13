
import bs4 
from bs4 import BeautifulSoup as bs
import requests
import time
import datetime
import pandas as pd

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect

# NASA Mars Top News
def mars_news(Browser):
    mars_news_url = "https://mars.nasa.gov/news"

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(mars_news_url)

    time.sleep(2)
    
    html = browser.html
    soup = bs(html, 'html.parser')

    try:
        news_title = soup.select_one("div.content_title a")
        print(news_title.text)

        news_text = soup.select_one("div.article_teaser_body")
        print(news_text.text)

        browser.quit()

        return news_title.text,news_text.text
    except:
        return None, None

# JPL Mars Space Images - Featured Image
def mars_featured_image(Browser):

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    space_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

    browser.visit(space_image_url)

    time.sleep(1)

    try:
        browser.links.find_by_partial_text('FULL IMAGE').click()

        html = browser.html
        soup = bs(html, 'html.parser')

        full_image_url = soup.find('img', class_="fancybox-image")

        # print(full_image_url['src'])

        featured_image_url = space_image_url.split("index.html")[0] + full_image_url['src']
        print(featured_image_url)

        browser.quit()

        return featured_image_url

    except:
        return None

# Mars Facts
def mars_facts(Browser):
    mars_fact_url = "https://space-facts.com/mars/"

    try:
        table = pd.read_html(mars_fact_url)
        df_mars_facts = table[0]

        df_mars_facts.columns=["Description", "Mars"]
        df_mars_facts = df_mars_facts.set_index(["Description"])

        print(df_mars_facts)

        # df_mars_facts.to_html('mars_facts_table1.html')

        return df_mars_facts.to_html(classes="table table-striped table-hover")

    except:
        return None

# Mars Hemispheres
def mars_hemispheres(Browser):

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    USGS_Astrogeology_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(USGS_Astrogeology_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    try:

        mars_hemisphere_links = soup.select("div.collapsible div a.itemLink")

        # mars_hemisphere_links
        time.sleep(1)  

        browser.quit()

        hemisphere_image_urls = []

        for link in mars_hemisphere_links:
        
            if(link.h3):

                url = USGS_Astrogeology_url.split("/search")[0] + link['href']

                executable_path = {'executable_path': ChromeDriverManager().install()}
                browser = Browser('chrome', **executable_path, headless=False)
            
                browser.visit(url)

                html = browser.html
                soup = bs(html, 'html.parser')

                time.sleep(1)
        
                title = soup.find("h2", class_="title")
                image_url = soup.find("a", text="Sample")
            
                print(title.text)
                print(image_url['href'])
                
                hemisphere_image_url = {}
                
                hemisphere_image_url["title"] = title.text
                hemisphere_image_url['image_url'] = image_url['href']
                
                hemisphere_image_urls.append(hemisphere_image_url)

                browser.quit()
                print(hemisphere_image_urls)

        return hemisphere_image_urls
    except:
        return None           
    
def scrape():

    mars_dict = {}
    news_title,news_text = mars_news(Browser)
    mars_dict['news_title'] = news_title
    mars_dict['news_text'] = news_text
    mars_dict['mars_featured_image'] = mars_featured_image(Browser)
    mars_dict['mars_facts'] = mars_facts(Browser)
    mars_dict['mars_hemispheres'] = mars_hemispheres(Browser)
    mars_dict['time_log'] = datetime.datetime.now()

    print(mars_dict)
    return mars_dict

# scrape()

