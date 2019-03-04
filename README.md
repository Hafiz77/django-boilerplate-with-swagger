## django-rest-framework-boilerplate with swagger
Simple boilerplate for django & django rest framework with swagger

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api-token-auth` | Request jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/user` | List users
POST | `/api/user/create` | Creates a user
GET | `/api/user/profile/{pk}` | Retrieve a user
PUT | `/api/user/update/{pk}` | Edit a user
DELETE | `/api/user/destroy/{pk}` | Delete a user


### Installation 
If you wish to run your own build, you two options
 1. User Docker compose.
    
    `$ git clone git@github.com:Hafiz77/django-boilerplate-with-swagger.git`
    
    `$ cd django-boilerplate-with-swagger`    
    `$ docker-compose up`
 
 2. Without docker
 
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

`pip install virtualenv`

Then, Git clone this repo to your PC

 `git clone git@github.com:Hafiz77/django-boilerplate-with-swagger.git`


`cd django-boilerplate-with-swagger`

Create a virtual environment

`python3 -m venv .venv && source .venv/bin/activate`


Install dependancies

`pip install -r requirements.txt`

Make migrations & migrate

`python3 ./manage.py makemigrations && python3 ./manage.py migrate`
Create Super user
    
`python3 manage.py createsuperuser`

### Launching the app
`python3 manage.py runserver`

### Run Tests
`python3 manage.py test`

### Swagger API Documentation

`http://localhost:8000/`