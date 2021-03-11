
import bs4 
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

from flask import Response
from flask import Flask, jsonify

from scrape_mars import scrape
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/<br/>"
        f"/scrape<br/>"
    )

@app.route("/scrape")
def scrape_data():
    return scrape()


if __name__ == '__main__':
    app.run(debug=True)