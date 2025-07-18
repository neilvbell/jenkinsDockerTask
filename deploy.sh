#!/bin/bash

# clean-up by deleting all current containers prior to running fresh each time
	docker rm -f $(docker ps -a)
# Create a Network
	docker network create my-network
#Create a volume

#Build flask-app and mysql images
	cd db/
	docker build -t mysql_img .
 	cd ..
  	cd flask-app/
	docker build -t flask_new_img .

#Run mysql container
	docker run -dit --network my-network --name mysql1 mysql_img
#Run flask-app container
	docker run -dit --network my-network --name flask-app flask_new_img

#Run nginx from official image (but need nginx.conf edited)
	cd ..
 	cd nginx/
	docker run -dit -p 80:80 --network my-network -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf --name nginx2 nginx
#Show all containers
	docker ps -a
exit 0
