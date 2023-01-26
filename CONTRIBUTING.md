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

## After creating user in {{app-name}} /models.py, go to {{project-name}}/settings.py and add

```
AUTH_USER_MODEL = '{{app-name}}.{{userModel-name}}'
```

## To create db migrations for app

```
python manage.py makemigrations {{app-name}}
```

## To udpate db with migrations for app

```
python manage.py migrate
```