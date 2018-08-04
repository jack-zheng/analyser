from flask import Blueprint
from flask import request, jsonify
from . import gitutil
from elasticsearch import Elasticsearch
from .config import Config
import json


essearch_bp = Blueprint('essearch', __name__)
es = Elasticsearch(getattr(Config, 'ESSEARCH_URL'))


@essearch_bp.route('/')
def index():
    return '<h1> Hello, this is essearch from blueprint</h1>'


@essearch_bp.route('/api/migrate', methods=['GET'])
def migrate_record():
    """
    API method to create migrate records to elastic search service
    """
    paths = gitutil.get_all_case_record_paths()
    rets = []
    for sub in paths:
        case = gitutil.parse_commit(sub)
        ret = insert_essearch_record(case)
        rets.append(ret)

    response = jsonify({"cases": rets})
    return response


@essearch_bp.route('/api/clean', methods=['GET'])
def remove_all_documents():
    ret = delete_essearch_record('author', '*')
    return jsonify(ret)


def insert_essearch_record(case):
    tmp = case.__dict__
    body = json.loads(json.dumps(tmp))
    return es.index(index=getattr(Config, 'index_type'),
             doc_type=getattr(Config, 'doc_type'),
             body=body)


def delete_essearch_record(field, match):
    return es.delete_by_query(index=getattr(Config, 'index_type'),
                doc_type=getattr(Config, 'doc_type'),
                body={"query": {"wildcard": {field: match}}})


def convert_json_to_obj(json, obj):
    """
    1. get attribute fileds form obj
    2. loop json fields get values
    3. assign values to obj
    """
    attrs = obj.__dict__
    for field in attrs:
        obj.__setattr__(field, json[field])