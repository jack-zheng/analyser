from app import app
from flask import request, abort, jsonify
from app.models import TestCase


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World from Analyser'


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
