# analyser

This repo is created for maintanence Qray daily job in a easy way, to save your time and life to do more mainingfful things.

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
+ flask docker image

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
