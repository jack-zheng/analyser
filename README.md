# Analyser

This repo is created for maintanence Qray daily job in a easy way, to save your time and life to do more mainingfful things.

## Usage

1. download this repo and cd to analyser
1. run command: `docker build -t analyzer .`  #this command will create a image you will run later
1. the first time run: `docker run -d -p 4000:80 --name analyzer_jk analyzer`
1. send post request to website to trigger history update `CURL -H "Content-Type:application/json" -X POST http://10.129.126.245:4000/webhook`

## Debug website without run docker

1. enable virtualenv
    * cd to project folder, run command 'pipenv shell'
1. start web service: flask run
    * it enable debug by default which is setting in file `.flaskenv`

## Debug Mode Class

1. fire virtual env 'pipenv shell' and 'ipython'
1. 'from app import db' and 'from app.models import TestCase'
1. test model method using 'TestCase.get_all()'

## Other Debug Tips

* export lib list to file: `pipenv lock -r > app/requirements.txt`

## Task List

**Enhance Member List Page**
1. add new member area above member list
1. edit button beside member record
1. delet button beside member record
1. able to copy to clipboard, format is 'username \<email addr\>'
1. pagation of members, previous - next button to navigate
1. test about csrf of wtf extension
1. login require when cud to user

### DB Migration

usage of alembic db management

1. when first time run, use: python manage_db.py db init  <- new migration folder

1. python manage_db.py db migrate --message 'some message you want'  <- add version info

1. python manage_db.py db upgrade, then the db schema will be changed  <- db level change, create/update db

1. python manage_db.py db history, to check the change history

1. when OS is windows, mirgate with --message will be failed

**PS:** SQLITE is not support the rename of column, so I have to do this db change manually
