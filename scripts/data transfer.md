# Steps

1. download download au-usermanagement repo under analyser
2. clean test_case table # delete from test_case;
3. reset commit_trace of test_case table #update sqlite_sequence set seq = 1 where name = 'CASE_INFO';
4. run python git_migration.py #Fetch commit info of au-usermanagement repo and insert them into test_case table
5. run python overwrite.py to update case info
