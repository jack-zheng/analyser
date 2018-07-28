from flask import Blueprint
from flask import request, jsonify
from app.models import TestCase

essearch_bp = Blueprint('essearch', __name__)


@essearch_bp.route('/')
def index():
    return '<h1> Hello, this is essearch from blueprint</h1>'

'''
API method to create a new record of github to elastic search service
'''
@essearch_bp.route('/api/record', methods=['GET', 'POST'])
def record():
    tmp = TestCase()
    ret = request.get_json()
    convert_json_to_obj(ret, tmp)

    # send result to es service
    
    response = jsonify(ret)
    response.status_code = 200
    return response


def convert_json_to_obj(json, obj):
    '''
    1. get attribute fileds form obj
    2. loop json fields get values
    3. assign values to obj
    '''
    attrs = obj.__dict__
    for field in attrs:
        obj.__setattr__(field, json[field])

def check_record(obj):
    '''
    check whether a record is a valid record
    '''
    # null point check, all fields should not be null
    pass