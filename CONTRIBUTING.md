# CONTRIBUTING

## How to create a django project in the same folder

```
django-admin startproject {{project-name}} .
```

## How to create an app inside the project

```
python manage.py startapp {{app-name}} 
```

## Add new apps to {{project-name}}/settings.py/INSTALLED_APPS
## For api

```
'rest_framework'
'rest_framework.authtoken'
'{{app-name}}'
```

## To run application

```
python manage.py runserver localhost:8000 [port is free choice]
```