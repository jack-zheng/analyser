# HOW TO UPDATE CASE INFO MANUALLY

1. download download au-usermanagement repo under analyser
2. fire sqlite3 terminal of analyzer::app::app.db
3. clean test_case table by run sql: `delete from test_case;`
4. reset commit_trace of test_case table by run sql: `update sqlite_sequence set seq = 0 where name = 'test_case';`
5. run `python git_migration.py` to fetch commit info of au-usermanagement repo and insert them into test_case table
6. fire sqlite3 terminal and run sql in rewrite.sql to upadte legacy svn history

PS: There are about 8 record, exit in backup table but not exist in test_case table, recheck them.

```sql
select * from case_backup cb left join test_case tc on tc.file_name = cb.file_name where tc.author is null;
```
