# Import Dependencies / Modules / Libraries
import pymongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape_mars

# Create flask app
app = Flask(__name__)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# create mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# client = pymongo.MongoClient()
# db = client.mars_db
# collection = db.mars_data_entries

# Create root to query mongoDB then pass data to HTML web display
@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    #marsdata = list(db.marsdata.find())
    return  render_template('index.html', mars_data=mars_data)

# Create root to scrape 
@app.route("/scrape")
def scraper():
    #db.mars_collection.remove({})
    mars_data = mongo.db.mars_data
    mars = scrape_mars.scrape()
    mars_data.update({}, mars, upsert=True)
    return redirect('http://localhost:5000/', code=302)
    # return "Scraping Successful"

if __name__ == "__main__":
    app.run(debug=True)