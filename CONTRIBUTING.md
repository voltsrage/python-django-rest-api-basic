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

## To create superuser

```
python manage.py createsuperuser
```

## After model is added, django admin needs to be notified, so go to {{app-name}}/admin.py

```
admin.site.register(models.UserProfile)
```

## To add views to project for API App, go to {{project-name}}/urls and add 

```
from django.urls import path,include

# a new path for the APIView
path('api/',include('{{app-name}}.urls'))
```

## To add urls to application go to {{app-name}} and add urls.py, then to urls.py add

```
from django.urls import path
from profiles_api import views

urlpatterns = [
	path('resource-name/', views.{{APIView-Name}}.as_view())
]

the above allow a user to get to resource by {{base_url}}/api/{{resource-name}}
```

## For viewsets in {{app-name}}/urls.py

```
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('{{resource-name}}', views.{{viewset-name}}, base_name='{{resource-name}}')

urlpatterns = [
	path('resource-name/', views.{{APIView-Name}}.as_view()),
	path('',include(router.urls))
]
```

## To test authentication install ModHeader Chrome extension
## Then in Request Headers

```
Name  					Value
Authorization   {{Token}}
```