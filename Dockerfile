FROM debian:9


#Install mongodb
RUN apt-get update
RUN apt-get install -y gnupg
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
RUN echo "deb http://repo.mongodb.org/apt/debian stretch/mongodb-org/3.6 main" | tee /etc/apt/sources.list.d/mongodb-org-3.6.list
RUN apt-get update
RUN apt-get install -y mongodb-org

#install python
RUN apt-get install -y python3 python3-pip


#mongodb setup
RUN mkdir /opt/db

#Set up app
WORKDIR /opt/vcp
COPY ./ /opt/vcp


#Start app
CMD ["./start.sh"]
