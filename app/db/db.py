from bson.errors import InvalidId
from bson.objectid import ObjectId
from flask import Flask, jsonify, request, json, abort
from flask_pymongo import PyMongo
import sys



# Adds a new startup to the platform
def add_startup(mongo, request_json):
    for u in mongo.db.startups.find():
        if u["name"] == request_json["name"]:
            return False;

    user_id = mongo.db.startups.insert({
        "name": request_json["name"],
    })

    return True;


if __name__ == "__main__":

    app = Flask(__name__)
    app.config['MONGO_DBNAME'] = 'vcpdb'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/vcp'
    mongo = PyMongo(app)

    with app.app_context():

        request_json = {"name": "Menu3"}
        print("Added startup: " + str(add_startup(mongo, request_json)))
