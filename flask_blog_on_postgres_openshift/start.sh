#openshift
oc get template postgresql-ephemeral -n openshift -o json > postgres.json

oc process -f postgres.json -p POSTGRESQL_USER=postgres1 -p POSTGRESQL_PASSWORD=postgres1 -p POSTGRESQL_DATABASE=posts_api -p DATABASE_SERVICE_NAME=postgres -l app=postgres | oc create -f -

oc new-app --as-deployment-config --name flask https://github.com/rasulkarimov/python --context-dir flask_blog_on_postgres_openshift/app/

flask db init
flask db migrate
flask db upgrade


oc new-app --as-deployment-config --name nginx https://github.com/rasulkarimov/python --context-dir flask_blog_on_postgres_openshift/nginx/


