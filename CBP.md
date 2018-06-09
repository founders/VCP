Configuring
------
No current config.

Building
-------
To build the docker container run

`docker build -t vcp .`

Deploy
-------
To deploy, get the docker container and run the following.

`docker run -v ./db:/opt/db vcp`


This will use the local `./db` as the directory for the mongodb data
