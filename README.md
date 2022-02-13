# 2022-django4-marketplace-jfu
MEMBUAT E-COMMERCE MARKETPLACE MENGGUNAKAN DJANGO VERSI 4

Gihub repository: https://github.com/gurnitha/2022-django4-marketplace-jfu


### 1. SETUP
------------


#### 1.1 Create github repository

        modified:   README.md


### 2. CREATE DJANGO PROJECT DAN APP
------------------------------------


#### 2.1 Membuat proyek dengan nama 'config'

        > (defatul-venv) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2.2 Membuat django app dengan nama 'app/marketplace'

        > (defatul-venv) λ mkdir app\marketplace
        > (defatul-venv) λ django-admin startapp marketplace app\marketplace

        new file:   app/marketplace/__init__.py
        new file:   app/marketplace/admin.py
        new file:   app/marketplace/apps.py
        new file:   app/marketplace/migrations/__init__.py
        new file:   app/marketplace/models.py
        new file:   app/marketplace/tests.py
        new file:   app/marketplace/views.py
        modified:   config/settings.py


### 3. DATABASE
---------------


#### 3.1 Create and connect with Postgres database

        > python -m pip install psycopg2
        > python -m pip install django-environ
        (defatul-venv) λ touch config\.env

        <!-- in .env file -->
        SECRET_KEY=keysmdfdfdfkd;lfkdlfkds;lfkds;lfkd;l
        DATABASE_NAME=db_name
        DATABASE_USER=postgres
        DATABASE_PASSWORD=xxxxxxx 

        <!-- in settings.py file -->
        import environ
        env = environ.Env()
        environ.Env.read_env()

        SECRET_KEY = env('SECRET_KEY');

        DATABASES = {
	        'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': env('DATABASE_NAME'),
	        'USERNAME': env('DATABASE_USER'),
	        'PASSWORD': env('DATABASE_PASSWORD'),
	        'HOST': 'localhost',
	        'PORT': '5432'
	        }
        }

        modified:   README.md
        modified:   config/settings.py


#### 3.2 Create superuser

        > (defatul-venv) λ python manage.py migrate
        > (defatul-venv) λ python manage.py createsuperuser
        
        Username (leave blank to use 'hp'): admin
        Email address: email@gmail.com
        Password:
        Password (again):
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.


### 4. DJANGO MODELS
--------------------


#### 4.1 Create Categoriers model

        modified:   README.md
        modified:   app/marketplace/admin.py
        new file:   app/marketplace/migrations/0001_initial.py
        modified:   app/marketplace/models.py