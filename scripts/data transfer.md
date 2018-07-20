# Steps

1. download PLT-User repo to analyser 
2. clean case_info and commit_trace column of app.db
    * reset sqlite_sequence table record
3. run python git_migration.py to insert git file info to app.db
4.