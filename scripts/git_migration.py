import os
import config
from git import Repo
from os import walk
from os.path import join
import sqlite3
from datetime import datetime

repo = Repo(config.git_repo)

def main():
	# log start time
	start = datetime.now()

	# get case info that we need to insert into db
	file_path = []
	folder_path = config.git_repo + config.case_folder
	print('folder path: %s ' % folder_path)
	for root, dirs, files in walk(folder_path):
		for file in files:
			file_path.append(os.path.abspath(join(root,file)))

	# print path for debug
	print('file path list size: %s' %len(file_path))

	# write records into db
	conn = sqlite3.connect(config.db_path)
	c = conn.cursor()

	for path in file_path:
		print('process path: %s' % path)
		r = parse_commit(path)
		sql = build_sql(r)
		print('execute record: %s' % sql)
		c.execute(sql)
		print('execute complete')

	conn.commit()
	conn.close()
	print('Finish migration!')

	# log end time
	end = datetime.now()
	print('Time Comsume: %s' % (end - start).seconds)

# insert record into db
def build_sql(record):
	return "INSERT INTO test_case ('{}', '{}', '{}', '{}', '{}', '{}') VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"\
	.format("FILE_NAME", "AUTHOR", "CREATE_DATE", "LAST_UPDATE_BY", "LAST_UPDATE_TIME", "FILE_PATH",\
		record.file_name, record.author, record.create_date, record.last_update_by, record.last_update_date, record.path)


# give a file path, return records object
def parse_commit(file_path):
	print("file_path: %s" %file_path)
	commits = list(repo.iter_commits(paths=file_path))
	path = file_path.replace('/Users/i306454/gitStore/analyser', '')
	print("path after lstrip: %s" % path)

	return Record(
		file_path.split('/')[-1],
		commits[-1].author.name,
		datetime.fromtimestamp(commits[-1].committed_date).strftime("%Y-%m-%d %H:%M:%S.%f"),
		commits[0].author.name,
		datetime.fromtimestamp(commits[0].committed_date).strftime("%Y-%m-%d %H:%M:%S.%f"),
		path
		)


class Record(object):
	"""docstring for records"""
	def __init__(self, file_name, author, create_date, last_update_by, last_update_date, path):
		self.file_name = file_name
		self.author = author
		self.create_date = create_date
		self.last_update_by = last_update_by
		self.last_update_date = last_update_date
		self.path = path

	def to_string(self):
		print('records defail: filename:%s, author:%s, create_date:%s, last_update_by:%s, last_update_date:%s, path:%s' \
			%(self.file_name, self.author, self.create_date, self.last_update_by, self.last_update_date, self.path))

if __name__ == '__main__':
	main()
