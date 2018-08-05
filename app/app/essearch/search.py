from flask import Blueprint
from flask import request, jsonify
from . import gitutil
from elasticsearch import Elasticsearch
from .config import Config
import json
import sqlite3


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


def svn_legacy_case_migrate():
    # get all records from legacy db and store them into a map
    # map = {
    #   case_name: {
    #       author:xxx, create_time: xxx
    #      }
    #  }
    conn = sqlite3.connect(getattr(Config, 'db_name'))
    cur = conn.cursor()
    sql = """select file.entry_id, file.file_name, log.date, log.revision, log.author
                from svn_files_info file,
                (select * from (select * from svn_log_entry order by revision desc) group by entry_id) log
            where log.entry_id = file.entry_id;"""

    cur.execute(sql)
    ret = cur.fetchall()
    conn.commit()
    conn.close()
    cases_map = {}
    for sub in ret:
        time = (sub[2]).split('.')[0]
        case_entry = {"author": sub[4], "create_date": time}
        cases_map[sub[1]] = case_entry

    return cases_map


@essearch_bp.route('/api/clean', methods=['GET'])
def remove_all_documents():
    ret = delete_essearch_record('author', '*')
    return jsonify(ret)


@essearch_bp.route('/api/search/<string:case_name>', methods=['GET'])
def search_record(case_name):
    ret = search_essearch_record("file_name", "*%s*" % case_name)

    response = jsonify(ret)
    return response


@essearch_bp.route('/api/test', methods=['GET'])
def get_first_essearch_record():
    ret = search_record("BulkImportDemo.java")
    print(json.loads(ret.data))
    return "123"


def update_essearch_record(id, entry):
    # pass id, author, create time and update accordingly
    ret = es.update(index=getattr(Config, 'index_type'),
                    doc_type=getattr(Config, 'doc_type'),
                    body={"doc": entry},
                    id=id)
    print("update record: %s" % ret)


def insert_essearch_record(case):
    tmp = case.__dict__
    body = json.loads(json.dumps(tmp))
    return es.index(index=getattr(Config, 'index_type'),
             doc_type=getattr(Config, 'doc_type'),
             body=body)


def delete_essearch_record(field, match):
    return es.delete_by_query(index=getattr(Config, 'index_type'),
                doc_type=getattr(Config, 'doc_type'),
                body={"query": {"wildcard": {field: match}}},
                ignore=[400, 404])


def search_essearch_record(field, match):
    match = match.lower()
    return es.search(index=getattr(Config, 'index_type'), body={"query": {"wildcard":{field: match}}})


def convert_json_to_obj(json, obj):
    """
    1. get attribute fileds form obj
    2. loop json fields get values
    3. assign values to obj
    """
    attrs = obj.__dict__
    for field in attrs:
        obj.__setattr__(field, json[field])