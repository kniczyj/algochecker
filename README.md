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



