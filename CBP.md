Configuring
------
No current config.

Building
-------
To build the docker container run

`docker build -t username/vcp .`

Deploy
-------
To deploy, get the docker using:

`docker pull vertoforce/vcp`

Run the container using the following.

`docker run --init -v /db:/opt/db -p 5000:5000 vcp`


This will use the local `/db` as the volume for the mongodb data
