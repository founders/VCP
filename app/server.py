import sys, os

from flask import Flask, jsonify, request, json, abort, render_template
from flask_pymongo import PyMongo
from pprint import pprint

from db.utilities import get_all_startups

app = Flask(__name__)


# ROUTING

# Serves homepage
@app.route("/")
def main():
    startups = get_all_startups(app.config['MONGO_INSTANCE'])
    return render_template('home.html', startups=startups)



# AJAX

# Serves homepage
@app.route("/data/startups/")
def fetch_startups():
    startups = get_all_startups(app.config['MONGO_INSTANCE'])
    startups_cleaned = [{'name': startup['name']} for startup in startups]
    return jsonify({'startups': startups_cleaned})



# MISCELLANIOUS

def run_server(db_name='vcp', db_uri='mongodb://localhost:27017/vcp', debug=False):
    app.config['MONGO_DBNAME'] = db_name
    app.config['MONGO_URI'] = db_uri
    mongo = PyMongo(app)
    app.config['MONGO_INSTANCE'] = mongo

    # NOTE: debug must be false to allow running as a separate thread
    app.run(debug=debug, host="0.0.0.0")


# NOTE: This will also run if run_server is created as a top-level process
if __name__ == '__main__':
    run_server('vcp', 'mongodb://localhost:27017/vcp', debug=True)
