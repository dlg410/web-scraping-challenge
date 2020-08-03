from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__, template_folder='template')

# conn = 'mongodb://localhost:27017/mars.app'
# client = pymongo.MongoClient(conn)

# db = client.mars_db

app.config['MONGO_URI'] = "mongodb://localhost:27017/mars.app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    print("Mars", mars)
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)