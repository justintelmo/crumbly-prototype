from flask import Flask, request, jsonify
from src import yelp

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World?'

@app.route('/yelp/<restaurant_name>')
def search_yelp(restaurant_name):
    restaurant = yelp.search_yelp(restaurant_name)
    return jsonify(restaurant)

if __name__ == '__main__':
    app.run()