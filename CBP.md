Configuring
------
No current config.

Building
-------
To build the docker container run

<<<<<<< HEAD
`docker build -t vcp .`

Deploy
-------
To deploy, get the docker container and run the following.

`docker run -v ./db:/opt/db vcp`


This will use the local `./db` as the directory for the mongodb data
=======
`docker build -t username/vcp .`

Deploy
-------
To deploy, get the docker using:

`docker pull vertoforce/vcp`

Run the container using the following.

`docker run --init -v /db:/opt/db -p 5000:5000 vcp`


This will use the local `/db` as the volume for the mongodb data
>>>>>>> 1abaf5278a4bf34580f2cdbe26ca18fd937982cd
