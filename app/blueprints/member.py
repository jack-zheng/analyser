from flask import Blueprint, render_template
from app.models import User


member_bp = Blueprint('member', __name__)


@member_bp.route('/list', methods=['GET'])
def list():
    users = User.query.all()
    return render_template('member/member_list.html', users=users)
