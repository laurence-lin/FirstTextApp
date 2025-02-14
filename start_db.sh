#!/bin/bash
docker network create textapp_network  # Choose a name for your network
docker run --name db --network textapp_network -e MYSQL_ROOT_PASSWORD=root123 -e MYSQL_USER=admin \
-e MYSQL_PASSWORD=laurence -e MYSQL_DATABASE=firsttext -v ./sql_scripts/init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 mysql:latest
docker run --network textapp_network -e DJANGO_SETTINGS_MODULE=firsttextproj.settings -p 8000:8000 -v .:/app django_app