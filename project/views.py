from project import app
from flask import request, abort, jsonify


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World'


@app.route('/qray/api/v1/<string:case_name>', methods=['GET'])
def get_task(case_name):
    results = {}
    results['name'] = case_name
    response = jsonify(results)
    response.status_code = 200
    return response