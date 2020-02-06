# algochecker - app for checking algorithms solutions



### Pre-docker app requirements for Ubuntu

```bash
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev

# create database in psql shell
CREATE DATABASE checkerDB;
CREATE USER checkerUser WITH PASSWORD 'password';
ALTER ROLE checkerUser SET client_encoding TO 'utf8';
ALTER ROLE checkerUser SET default_transaction_isolation TO 'read committed';
ALTER ROLE checkerUser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE checkerDB TO checkerUser;

# if no venv create it. Then install requiremets

pip3 install -r requirements.txt

# run migrations in app root directory

python3 manage.py runmigrations
```



