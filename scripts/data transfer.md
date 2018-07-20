# Steps

1. download PLT-User repo to analyser 
2. clean case_info and commit_trace column of app.db
    * reset sqlite_sequence table record
3. run python git_migration.py => insert git file info to app.db
4. run python update_case_info.py => update git file record, correct legacy case info
5. run python transfer_data_to_app.py => migrate case info to analyser/app/app.db, task finished