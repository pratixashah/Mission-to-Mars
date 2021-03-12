
import bs4 
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
from flask import Response
from flask import Flask, jsonify
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import scrape_mars
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)