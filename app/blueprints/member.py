from flask import Blueprint, render_template, request, jsonify
from app.models import User
from app.extensions import db
import os


member_count_per_page = int(os.getenv('member_count_per_page', '8'))
member_bp = Blueprint('member', __name__)


@member_bp.route('/list', methods=['GET'])
def list():
    '''
    This route will return the page contains the default paginate obj to show
    in page. and about the paginate obj refresh, we handle it by using Ajax.
    '''
    paginate = User.query.paginate(1, member_count_per_page, False)
    return render_template('member/member_list.html', paginate=paginate)


# the way to enable multiple route.
# @member_bp.route('/paginate', defaults={'page_num': 2}, methods=['GET'])
@member_bp.route('/paginate/<int:page_num>', methods=['GET'])
def paginate_obj(page_num):
    paginate = User.query.paginate(page_num, member_count_per_page, False)
    return render_template('member/member_table.html', paginate=paginate)


@member_bp.route('/delete/<uid>', methods=['GET', 'POST'])
def delete(uid):
    if request.method == 'POST':
        if not uid:
            return "Empty UID", 400
        User.query.filter_by(id=uid).delete()
        db.session.commit()
        return "Success", 200
    else:
        return "Not Support", 405


@member_bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        user = request.get_json()
        if not user['id']:
            return "Empty UID", 400
        tmp = User.query.filter_by(id=user['id'])[0]
        tmp.username = user['username']
        tmp.email = user['email']
        db.session.add(tmp)
        db.session.commit()
        response = jsonify(
            {"id": tmp.id, "username": tmp.username, "email": tmp.email})
        response.status_code = 200
        return response
    else:
        return "Not Support", 405
