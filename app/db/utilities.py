from bson.errors import InvalidId
from bson.objectid import ObjectId
from flask import Flask, jsonify, request, json, abort
from flask_pymongo import PyMongo
import sys

from pprint import pprint


# STARTUPS



# Retrieves all startups on the platform
def get_all_startups(mongo):
    return list(mongo.db.startups.find())

# Adds a new startup to the platform
def add_startup(mongo, request_json):
    startup = mongo.db.startups.find_one({"name": request_json["name"]})
    if startup is not None:
        return False
    startup_id = mongo.db.startups.insert({
        "name": request_json["name"],
    })
    return True

# Modifies the data of a startup
# NOTE: All data passed in to request_json will overwrite old data
# NOTE: If the startup needs to be renamed, enter the new name in the new_name field of request_json
def update_startup(mongo, request_json):
    startup = mongo.db.startups.find_one({"name": request_json["name"]})
    if startup is None:
        return False
    if request_json.get("new_name") is not None and mongo.db.startups.find_one({"name": request_json["new_name"]}) is not None:
        return False
    mongo.db.startups.update_one({
        "_id": startup["_id"]},
        {"$set": {"name": request_json["new_name"]}
        }, True)
    return True

# Removes a startup from the platform
def remove_startup(mongo, request_json):
    startup = mongo.db.startups.find_one({"name": request_json["name"]})
    if startup is None:
        return False
    mongo.db.startups.remove(startup["_id"])
    return True



if __name__ == "__main__":

    app = Flask(__name__)
    app.config['MONGO_DBNAME'] = 'vcpdb'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/vcp'
    mongo = PyMongo(app)

    with app.app_context():
        # Test adding startups
        request_json = {"name": "Menu3"}
        print("Added startup: " + str(add_startup(mongo, request_json)))
        request_json = {"name": "Menu3"}
        print("Added startup: " + str(add_startup(mongo, request_json)))  # Should fail: duplicate
        request_json = {"name": "Vitrix Health"}
        print("Added startup: " + str(add_startup(mongo, request_json)))

        # Test retrieving startups
        pprint(get_all_startups(mongo))

        # Test updating startups
        request_json = {"name": "Menu3", "new_name": "Agrimy"}
        print("Updated startup: " + str(update_startup(mongo, request_json)))
        request_json = {"name": "Vitrix Health", "new_name": "Agrimy"}
        print("Updated startup: " + str(update_startup(mongo, request_json)))  # Should fail: duplicate

        # Test removing startups
        request_json = {"name": "Agrimy"}
        print("Removed startup: " + str(remove_startup(mongo, request_json)))
        request_json = {"name": "Vitrix Health"}
        print("Removed startup: " + str(remove_startup(mongo, request_json)))
        request_json = {"name": "Menu3"}
        print("Removed startup: " + str(remove_startup(mongo, request_json)))  # Should fail: doesn't exist
