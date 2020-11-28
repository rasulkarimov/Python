#openshift
oc get template postgresql-ephemeral -n openshift -o json > postgres.json

oc process -f postgres.json -p POSTGRESQL_USER=postgres1 -p POSTGRESQL_PASSWORD=postgres1 -p POSTGRESQL_DATABASE=posts_api -p DATABASE_SERVICE_NAME=postgres | oc create -f -

oc new-app --as-deployment-config --name flask https://github.com/rasulkarimov/python#blog_on_postgres_openshift --context-dir=flask_blog_on_postgres/app/ 

oc new-app --name flask https://github.com/rasulkarimov/python#blog_on_postgres_openshift --context-dir flask_blog_on_postgres/app/



