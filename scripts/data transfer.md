# Steps

1. download download au-usermanagement repo under analyser
2. clean test_case table # delete from test_case;
3. reset commit_trace of test_case table #update sqlite_sequence set seq = 0 where name = 'test_case';
4. run python git_migration.py #Fetch commit info of au-usermanagement repo and insert them into test_case table
5. run sql to rewrite author, create_date of test_case table


PS: There are about 8 record, exit in backup table but not exist in test_case table, recheck them.
```sql
select * from case_backup cb left join test_case tc on tc.file_name = cb.file_name where tc.author is null;
```
