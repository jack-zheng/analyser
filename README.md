# Analyser

This repo is created for maintanence Qray daily job in a easy way, to save your time and life to do more mainingfful things.

## Usage

1. download this repo
2. cd analyser
3. run command: `docker build -t <image name> .`  #this command will create a image you will run later
4. the first time run: `docker run -p 4000:80 --name <container name> <image name>`
5. `docker start <container name>` #run this command if the container is down

## Debug website without run docker

1. enable virtualenv
    * cd to project folder, run command 'pipenv shell'
2. special the run file to start local website: export FLASK_APP=local_run.py
3. open debug mode and you can modify your code in fly: export FLASK_ENV=development
4. start web service: flask run

## Task List

**Backlog:**

single script to finish new case migrate(function under script folder)

### DB Migration

usage of alembic db management

1. when first time run, use: python manage_db.py db init  <- new migration folder

2. python manage_db.py db migrate --message 'some message you want'  <- add version info 

3. python manage_db.py db upgrade, then the db schema will be changed  <- db level change, create/update db

4. python manage_db.py db history, to check the change history

5. when OS is windows, mirgate with --message will be failed

**PS:** SQLITE is not support the rename of column, so I have to do this db change manually
