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