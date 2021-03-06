from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import UpdateForm
from app.extensions import db
from app.models import TestCase, JobHistory
from datetime import datetime
from flask import request, abort, jsonify
from git import Repo
from os import walk
from os.path import join
import os
import logging
import re
import shutil


history_bp = Blueprint('history', __name__)


@history_bp.route('/', methods=['GET', 'POST'])
def hello():
    last_run = JobHistory.query.order_by(
        JobHistory.timestamp.desc()).first()
    form = UpdateForm()
    if form.validate_on_submit():
        flash('Update finished in %s sec.' % update_history(), 'success')
        return redirect(url_for('history.hello'))
    return render_template(
        'history/index.html', form=form,
        time=last_run.timestamp if last_run else [])


@history_bp.route('/apacheclient', methods=['GET'])
def apacheclient():
    shutil.rmtree('./au-usermanagement')
    logging.warning('Git Repo Deleted!')
    return "Success", 200


def update_git_history_job():
    with db.app.app_context():
        update_history()


def update_history():
    start = datetime.now()
    # Steps to update git history to db
    # 1. clone/pull repo
    webhookrepo = ''
    repopath = './au-usermanagement'
    if os.path.isdir(repopath):
        # after update, remove git repo
        shutil.rmtree(repopath)
        logging.warning('Git Repo Deleted!')
    webhookrepo = Repo.clone_from(
        url=os.getenv('clone_url'), to_path=repopath)
    logging.warning('Finish Clone!')

    # 2. clean db data
    #       * delete all records from test_case table
    #       * update slqite_sequence table to reset test_case table
    #       auto increment count
    count = TestCase.query.delete()
    db.session.commit()
    logging.warning('Finish Clean DB! %s records been deleted.' % count)

    # 3. update test case info
    #       * loop git repo, update history of test case to test_case table
    #       * over write info of case_backup to test_case
    file_path = []
    folder_path = repopath + '/au-usermanagement-runtimetest/src/'\
        'main/java/com/successfactors/usermanagement/qray/cases'
    logging.warning('folder path: %s ' % folder_path)
    for root, dirs, files in walk(folder_path):
        for file in files:
            file_path.append(os.path.abspath(join(root, file)))

    logging.warning('[%s] records will be inserted' % len(file_path))

    insertrows = []
    for path in file_path:
        prefix = path.split('au-usermanagement')[0]
        commits = list(webhookrepo.iter_commits(paths=path))

        fname = path.split('/')[-1]
        # the username format is not unique, may be number or just name
        # so if the name is not id, use email address instead.
        author = get_user_id(commits[-1])
        cdate = datetime.fromtimestamp(commits[-1].committed_date)
        lby = get_user_id(commits[0])
        ldate = datetime.fromtimestamp(commits[0].committed_date)
        relative_path = path.replace(prefix, '', 1)

        case = TestCase(file_name=fname,
                        author=author,
                        create_date=cdate,
                        last_update_by=lby,
                        last_update_time=ldate,
                        file_path=relative_path)
        insertrows.append(case)

    db.session.add_all(insertrows)
    db.session.commit()

    logging.warning('Start Recover SVN History!')
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
    logging.warning('History Update Finished!')

    record = JobHistory(timestamp=datetime.utcnow())
    db.session.add(record)
    db.session.commit()
    return (datetime.now() - start).seconds


@history_bp.route('/webhook', methods=['GET', 'POST'])
def webhook():
    '''
    Webhook to trigger git history update.
    1. regist webhook on repo -> setting -> webhook
    2. add route in you website and business code when hook triggered

    [Warning!!!] since I got no permission to create a webhook to official
    repo, I leave this interface, and trigger the udpate manually.
    '''
    if request.method == 'POST':
        gap = update_history()
        return "Git records have updated in %s sec!" % gap, 200
    else:
        return 'Get request triggered', 200


@history_bp.route('/qray/api/v1/<string:case_name>', methods=['GET'])
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


def get_user_id(commit):
    '''
    return user id.
    regex to match id format like: C111111, if author name is not id, use email
    as key to get user id.
    '''
    match = r'\w\d+'

    if re.search(match, commit.author.name):
        return commit.author.name

    return os.getenv(commit.author.email) if os.getenv(commit.author.email)\
        else commit.author.email
