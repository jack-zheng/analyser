from flask import Blueprint


member_bp = Blueprint('member', __name__)


@member_bp.route('/list', methods=['GET'])
def list():
    return '''
    <h1>show member list here</h1>
    '''