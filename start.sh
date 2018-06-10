#!/bin/bash

# start mongodb
mongod --dbpath /opt/db &

# Wait for mongodb start
sleep 5

# start flask app
python3 app/server.py
