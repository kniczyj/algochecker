# algochecker - app for checking algorithms solutions



### Dockerized app (current state)

```bash
docker-compose up

# get into app container and run migrations
docker exec -it algochecker_web_1 bash
python3 manage.py migrate

# create superuser
python3 manage.py createsuperuser
```



### Pre-docker app requirements for Ubuntu

```bash
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev

# create database in psql shell
sudo -i -u postgres # switch user
psql  # enter shell
CREATE DATABASE checkerDB;
CREATE USER checkerUser WITH PASSWORD 'password';
ALTER ROLE checkerUser SET client_encoding TO 'utf8';
ALTER ROLE checkerUser SET default_transaction_isolation TO 'read committed';
ALTER ROLE checkerUser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE checkerDB TO checkerUser;

# if no venv create it. Then install requiremets

pip3 install -r requirements.txt

# run migrations in app root directory

python3 manage.py migrate
```



### Planner directory structure



.
├── **algochecker**
│   ├── asgi.py
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── checker
│   ├── admin.py
│   ├── apps.py
│   ├── init.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20200207_1353.py
│   │   ├── init.py
│   │   └── pycache
│   │       ├── 0001_initial.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── pycache
│   │   ├── admin.cpython-37.pyc
│   │   ├── apps.cpython-37.pyc
│   │   ├── init.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── **common_resources**
│   └── img
├── **compilation_runner**
│   ├── Dockerfile
│   └── src
├── docker-compose.yml
├── Dockerfile
├── **judge**
│   ├── Dockerfile
│   └── src
├── manage.py
├── media
│   └── uploads
│       ├── in
│       └── out
├── README.md
├── requirements.txt
├── templates
└── venv
    ├── bin
    │...