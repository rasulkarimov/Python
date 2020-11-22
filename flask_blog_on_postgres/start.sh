#!/bin/bash

# starting pod
sudo podman pod create --name blog_pod -p 80:80

#starting postgres in pod
sudo podman run -d --pod blog_pod -e POSTGRESQL_USER=postgres1 -e POSTGRESQL_PASSWORD=postgres1 -e POSTGRESQL_DATABASE=posts_api docker.io/centos/postgresql-12-centos7

#starting flask
sudo podman run -d --name flask_blog --pod blog_pod flask_blog

#starting nginx
sudo podman run -d --name nginx_blog --pod blog_pod nginx_blog

#initilize db
sudo podman exec flask_blog flask db init
sudo podman exec flask_blog flask db migrate
sudo podman exec flask_blog flask db upgrade

#openshift
oc get template postgresql-ephemeral -n openshift -o json > postgres.json

oc process -f postgres.json -p POSTGRESQL_USER=postgres1 -p POSTGRESQL_PASSWORD=postgres1 -p POSTGRESQL_DATABASE=posts_api -p DATABASE_SERVICE_NAME=postgres | oc create -f -


