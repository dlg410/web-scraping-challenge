from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017/mars.app'
client = pymongo.MongoClient(conn)

db = client.mars_db

@app.route('/')
def index():
    mars_info = list(mongo.db.mars_info.find())[0]
    print("Mars Info", mars_info)
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)