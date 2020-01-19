## For Reference. Shell commands for Django

* installing django rest framework
```
pipenv install djangorestframework
```
* activate virtual enviroment
```
pipenv shell
```
* start django project
```
django-admin startproject api_example
```
* migrate models
```
python manage.py migrate
```
* creating super user
```
python manage.py createsuperuser
```


### Making a model and migration
```
python manage.py makemigrations
```
```
python manage.py migrate
```

serializer deserializes the combination of lists and dictionaries into the application object/model
Translates to and from JSON

### Starting server

* Start virtual enviroment
* CD into api_example
* Run:
```
python manage.py runserver
```