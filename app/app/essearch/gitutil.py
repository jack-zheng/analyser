import os
from git import Repo
from os import walk
from os.path import join
from datetime import datetime
from ...models import TestCase

git_repo='/Users/i306454/gitStore/analyser/PLT-User'
case_folder='/src/com/successfactors/test/qray/cases/plt/usermanagement'

repo = Repo(git_repo)

def test():
    file_path = []
    folder_path = git_repo + case_folder
    print('folder path: %s ' % folder_path)
    for root, dirs, files in walk(folder_path):
        for file in files:
            file_path.append(os.path.abspath(join(root,file)))
    print("file count: %s" %len(file_path))

    case = parse_commit(file_path[0])
    print("case info: %" % case)

# give a file path, return records object
def parse_commit(file_path):
    commits = list(repo.iter_commits(paths=file_path))
    path = file_path.lstrip(os.path.abspath('.'))

    return TestCase(
        file_path.split('/')[-1],
        commits[-1].author.name,
        commits[-1].committed_date,
        commits[0].author.name,
        commits[0].committed_date,
        path)

if __name__ == "__main__":
    print("invoked")
    test()