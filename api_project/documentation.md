# django-admin startproject advanced_api_project

# cd advanced_api_project

# django-admin startapp api

# py manage.py runserver

# py manage.py makemigrations

# py manage.py migrate

# py manage.py createsuperuser

# py manage.py test ==> allows you to run your test

# To activate virtual environment

# py -m venv env

# env\Scripts\activate

#### when you see this error, how it was resolved

## when endpoint returned "detail": "Authentication credentials were not provided."

## ensure you add below code to settings.py

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
'rest_framework.authentication.TokenAuthentication',
],
'DEFAULT_PERMISSION_CLASSES': [
'rest_framework.permissions.IsAuthenticated',
],
}

## when an endpoint returned 404 not found check the urls.py and urlpatterns for the trailing /

## e.g path('profile', profile.as_view(), name='proffile') ensure you add 'profile/'

# set git global congif
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
