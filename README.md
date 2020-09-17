# Thetask

![Badge](https://img.shields.io/badge/python-3.8-blue.svg)
![Badge](https://img.shields.io/badge/django-3.1-bold.svg)



Live On Heroku

http://thetask-app-name.herokuapp.com/


### DEPLOYMENT STEPS

#### Create a .env file and fill with parameters
```bash
$ sudo cp .env-example .env
```

#### Build docker images
```bash
$ docker-compose up -d --build
```

#### go in docker db image and set user's password
```bash
$ docker-compose exec db psql --username=${username} --dbname=${dbname}
${dbname}# alter role ${username} with password 'yourdbpassword';
${dbname}# \q

```

#### Check migration 
```bash
$ docker-compose exec web python manage.py migrate --noinput
```

#### Start docker 
```bash
$ docker-compose up
```



Directory layout
================

Thetasks's directory structure looks as follows::

    thetask/
    ├── thetask
    │   ├── __init__.py
    │   ├── settingsa.py
    │   ├── asgi.py
    │   ├── urls.py    
    │   ├── wsgi.py
    └── apps
    │   ├── payment
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── stripe.py
    │   │   ├── urls.py
    │   │   ├── views.py
    │   │   │── migrations
    │   │   └── 0001.initial.py
    │   │   └── 0002.paymentlog_user.py
    │   ├── subscription
    │   │    ├── __init__.py
    │   │    ├── admin.py
    │   │    ├── apps.py
    │   │    ├── book_api.py
    │   │    ├── models.py
    │   │    ├── serializers.py
    │   │    ├── tests.py
    │   │    ├── views.py
    │   │    │── migrations
    │   │       └── 0001.initial.py
    │   │       └── 0002.subscrption_subscriber.py
    │   └── user
    │        ├── __init__.py
    │        ├── admin.py
    │        ├── apps.py
    │        ├── forms.py
    │        ├── models.py
    │        ├── serializers.py
    │        ├── tests.py
    │        ├── views.py
    │        ├── urls.py
    │        │── migrations
    │           └── 0001.initial.py
    │
    └── static
        └── ...
    └── templates
        └── ...
    └── thetask
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    └── .env-example
    └── .gitignore
    └── docker-compose.yml
    └── Dockerfile
    └── LICENCE
    └── manage.py
    └── README.md
    └── requirements.txt


Licence
================
MIT
