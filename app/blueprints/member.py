from flask import Blueprint, render_template
from app.models import User


member_bp = Blueprint('member', __name__)


@member_bp.route('/list', methods=['GET'])
def list():
    '''
    This route will return the page contains the default paginate obj to show
    in page. and about the paginate obj refresh, we handle it by using Ajax. 
    '''
    paginate = User.query.paginate(1, 3, False)
    return render_template('member/member_list.html', paginate=paginate)


# the way to enable multiple route.
# @member_bp.route('/paginate', defaults={'page_num': 2}, methods=['GET'])
@member_bp.route('/paginate/<int:page_num>', methods=['GET'])
def paginate_obj(page_num):
    paginate = User.query.paginate(page_num, 3, False)
    return render_template('member/member_table.html', paginate=paginate)
