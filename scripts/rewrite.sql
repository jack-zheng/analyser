update
	test_case
set author=(select case_backup.author from case_backup
	where test_case.file_name=case_backup.file_name),
create_date=(select case_backup.create_date from case_backup
	where case_backup.file_name=test_case.file_name)
where EXISTS (SELECT case_backup.file_name
                  FROM case_backup
                  WHERE case_backup.file_name = test_case.file_name);