# analyser
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
** AD Hoc Task:**
+ ~~migrate git to dev branch, update config~~
+ update new cases info after migration
+ daily case info update
+ web hook case info update

** Feature Backup **
+ Integrate with Swagger

**Feature backup: enhance show out of case author **
+ investigate about user info fetching(Confluence/Jira/Outlook)
+ change show out to user name instead of I number(New page for this, seems interesting)

**Feature backup: enhance case update **
+ about the impl of case info update
  - long term, update by check commit info
  - short term, everytime refresh db, update case
+ short term first
  git lib, update repo, insert record
  
**Feature backup: log mechanism **
+ if necessary, store log to file

### DB Migration
usage of alembic db management
+ when first time run, use: python manage_db.py db init  <- new migration folder
+ python manage_db.py db migrate --message 'some message you want'  <- add version info 
+ python manage_db.py db upgrade, then the db schema will be changed  <- db level change, create/update db
+ python manage_db.py db history, to check the change history
+ when OS is windows, mirgate with --message will be failed

**PS:** SQLITE is not support the rename of column, so I have to do this db change manually
