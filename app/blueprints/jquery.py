from flask import Blueprint, render_template, request
from app.forms import JQueryForm
from datetime import datetime


jquery_bp = Blueprint('jquery', __name__)


@jquery_bp.route('/get', methods=['GET', 'POST'])
def get():
    print(request.method)
    form = JQueryForm()
    if form.validate_on_submit():
        uesrname = form.username.data
        password = form.password.data
        return render_template(
            'jquery/get.html', form=form, content=[uesrname, password])
    return render_template('jquery/get.html', form=form)


@jquery_bp.route('/ajax_get', methods=['GET'])
def ajax_get():
    time = datetime.utcnow()
    return '<p>%s</p>' % time


@jquery_bp.route('/ajax_post', methods=['POST'])
def ajax_post():
    return 'Name: %s, Status: %s' % (request.form['name'], 200)
