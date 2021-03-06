from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import time
import scrape_mars
app = Flask(__name__)

# Databse connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html",mars=mars, planet = "Mars")

@app.route("/scrape")
def scraper():
     mars = mongo.db.mars
     mars_data = scrape_mars.scrape()
     mars.update({}, mars_data, upsert=True)
     return redirect("/", code=302)

 
if __name__ == "__main__":
    app.run(debug=True)


    