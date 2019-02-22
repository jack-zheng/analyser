from app import app, db
from app.models import TestCase
from datetime import datetime
from flask import request, abort, jsonify
from git import Repo
from os import walk
from os.path import join
import os
from dotenv import load_dotenv


load_dotenv()


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World from Analyser'


@app.route('/apacheclient', methods=['POST'])
def apacheclient():
    """
    Test API for reading Apache HttpClient source code
    :return: json context of request body
    """
    if not request.json:
        abort(400, "Not a json format")
    print(request.json)
    return jsonify(request.json)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    '''
    Webhook to trigger git history update.
    1. regist webhook on repo -> setting -> webhook
    2. add route in you website and business code when hook triggered
    '''
    if request.method == 'POST':
        # Steps to update git history to db
        # 1. clone/pull repo
        webhookrepo = ''
        repopath = './au-usermanagement'
        if not os.path.isdir(repopath):
            webhookrepo = Repo.clone_from(url=os.getenv('clone_url'), to_path=repopath)
            print('Finish Clone!')
        else:
            webhookrepo = Repo(repopath)
            webhookrepo.remotes.origin.pull()
            print('Finish Pull')

        # 2. clean db data
        #       * delete all records from test_case table
        #       * update slqite_sequence table to reset test_case table
        #       auto increment count
        TestCase.delete_all()
        db.session.execute(
            "update sqlite_sequence set seq = 0 where name = 'test_case'")
        db.session.commit()
        print('Finish Clean DB!')

        # 3. update test case info
        #       * loop git repo, update history of test case to test_case table
        #       * over write info of case_backup to test_case
        file_path = []
        folder_path = repopath + '/au-usermanagement-runtimetest/src/'\
            'main/java/com/successfactors/usermanagement/qray/cases'
        print('folder path: %s ' % folder_path)
        for root, dirs, files in walk(folder_path):
            for file in files:
                file_path.append(os.path.abspath(join(root, file)))

        print('[%s] records will be inserted' % len(file_path))

        insertrows = []
        for path in file_path:
            prefix = path.split('au-usermanagement')[0]
            commits = list(webhookrepo.iter_commits(paths=path))

            fname = path.split('/')[-1]
            author = commits[-1].author.name
            cdate = datetime.fromtimestamp(commits[-1].committed_date)
            lby = commits[0].author.name
            ldate = datetime.fromtimestamp(commits[0].committed_date)
            relative_path = path.replace(prefix, '')

            case = TestCase(file_name=fname, author=author, create_date=cdate,
                            last_update_by=lby, last_update_time=ldate,
                            file_path=relative_path)
            insertrows.append(case)

        db.session.add_all(insertrows)
        db.session.commit()

        print('Start Recover SVN History!')
        sql = '''
        update
            test_case
        set author=(select case_backup.author from case_backup
        where test_case.file_name=case_backup.file_name),
            create_date=(select case_backup.create_date from case_backup
        where case_backup.file_name=test_case.file_name)
        where EXISTS (SELECT case_backup.file_name
        FROM case_backup
        WHERE case_backup.file_name = test_case.file_name)'''
        db.session.execute(sql)
        db.session.commit()

        return "Finish Process Post Request!", 200
    else:
        return 'Get request triggered', 200


@app.route('/qray/api/v1/<string:case_name>', methods=['GET'])
def get_task(case_name):
    ret = TestCase.get_case_info(case_name)
    if not ret:
        abort(404, 'No Such Case In DB')

    cases = []
    for sub in ret:
        results = convert_sqlalchemy_to_json(sub)
        cases.append(results)
    response = jsonify({"cases": cases})
    response.status_code = 200
    return response


def convert_sqlalchemy_to_json(row):
    popkey = '_sa_instance_state'
    tmp = row.__dict__
    tmp.pop(popkey)
    return tmp
