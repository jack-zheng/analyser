# analyser
This repo is created for maintanence Qray daily job in a easy way, to save your time and life to do more mainingfful things.

## Usage
1. download this repo
2. cd analyser
3. run command: `docker build -t <image name> .`  #this command will create a image you will run later
4. the first time run: `docker run -p 4000:80 --name <container name> <image name>`
5. `docker start <container name>` #run this command if the container is down

## Phase II
**Feature 01: enhance show out of case author**
+ investigate about user info fetching(Confluence/Jira/Outlook)
+ change show out to user name instead of I number

**Feature 02: enhance case update**
+ about the impl of case info update
  - long term, update by check commit info
  - short term, everytime refresh db, update case
+ short term first
  git lib, update repo, insert record
  
**Feature 03: log mechanism**
+ if necessary, store log to file

## Phase I
+ ~ensure db structure to store SVN repo case info~
+ ~fetch info of SVN repo and store to sqlite db~
+ ~ensure db structure to store git repo case info~
+ ~fetch info from git repo and store to sqlite db~
+ ~merge info of this two table~
all above almost done in my part time project
+ ~add file path info into case_info table when process git_migration.py~

+ ~flask setup~
+ ~do data migration again~
+ ~flask API~
+ ~local service setup~
+ ~uwsgi docker image investigation~
+ ~nginx docker image investigation~
+ ~flask docker image~

### Add Flask To Runtime 
1. enable virtualenv
2. export FLASK_APP=local_run.py
3. export FLASK_ENV=development  <- enable debug mode

### DB Migration
usage of alembic db management
+ when first time run, use: python manage_db.py db init  <- new migration folder
+ python manage_db.py db migrate --message 'some message you want'  <- add version info 
+ python manage_db.py db upgrade, then the db schema will be changed  <- db level change, create/update db
+ python manage_db.py db history, to check the change history
+ when OS is windows, mirgate with --message will be failed
PS: SQLITE is not support the rename of column, so I have to do this db change manually
