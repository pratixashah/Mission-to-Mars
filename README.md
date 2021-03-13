# Web-Scraping
 
A web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

# Missions_to_Mars(dir) contains:

## Mission_to_Mars.ipynb: Includes all of scraping and analysis tasks listed below.

**1. NASA Mars News:** Scrapes the NASA Mars News Site(https://mars.nasa.gov/news) and collect the latest News Title and Paragraph Text.

**2. JPL Mars Space Featured Image:** finds the image url for the full size Featured Mars Image from Jet Propulsion Laboratory site(https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)

**3. Mars Facts:** Scrapes https://space-facts.com/mars/ for the table containing facts about the planet including Diameter, Mass, etc.

**4. Mars Hemispheres:** Use https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar’s hemispheres. These obtained by clicking each of the links to the hemispheres in order to find the image url to the full resolution image. Stores both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name in dictionary.

## scrape_mars.py: 
A Python script with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data

## app.py: 
Uses MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

**1. /scrape** uses scrape_mars.py script and call scrape function. Stores the return value in Mongo as a Python dictionary.

**2. /** uses query Mongo database and pass the mars data into an HTML template to display the data.

## index.html:
HTML file that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 











 
