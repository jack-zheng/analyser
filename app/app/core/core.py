from flask import Blueprint


core_bp = Blueprint('core', __name__)


@core_bp.route('/')
def index():
    return '<h1> This is Home Page</h1>'