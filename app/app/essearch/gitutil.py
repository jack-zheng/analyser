import os
from git import Repo
from os import walk
from os.path import join
from app.models import TestCase
from .config import Config


repo = Repo(getattr(Config, "git_repo"))


# return file path by which we can track commit info
def get_all_case_record_paths():
    file_path = []
    folder_path = getattr(Config, 'git_repo') + getattr(Config, 'case_folder')
    print('folder path: %s ' % folder_path)
    for root, dirs, files in walk(folder_path):
        for file in files:
            file_path.append(os.path.abspath(join(root,file)))
    return file_path


# give a file path, return records object
def parse_commit(file_path):
    commits = list(repo.iter_commits(paths=file_path))
    path = file_path.replace(getattr(Config, 'git_repo'), '')

    return TestCase(
        file_path.split('/')[-1],
        commits[-1].author.name,
        commits[-1].committed_date,
        commits[0].author.name,
        commits[0].committed_date,
        path)
