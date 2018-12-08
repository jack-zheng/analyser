# Steps

1. download PLT-User repo to analyser 
2. clean case_info and commit_trace column of app.db
    * reset sqlite_sequence table record(update sqlite_sequence set seq = 1 where name = 'CASE_INFO';)
3. run python git_migration.py #Fetch commit info of PLT_USER repo and insert them into case_info table
4. run python update_case_info.py #Fetch SVN check in info and rewrite author, date info of case_info table
5. run python transfer_data_to_app.py #The db structure of website is diff with the one we used here, so I write a transfer script to finish the data transfer