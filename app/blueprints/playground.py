from flask import Blueprint, render_template, flash
from app.forms import PlayGroundForm
from datetime import datetime


playground_bp = Blueprint('playground', __name__)


@playground_bp.route('/form', methods=['GET', 'POST'])
def show_submitted():
    form = PlayGroundForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        flash('You input has received!')
        return render_template(
            'playground/index.html', form=form, content=[name, body])
    return render_template('playground/index.html', form=form)


@playground_bp.route('/time', methods=['GET', 'POST'])
def show_time():
    return render_template(
        'playground/time.html', time=datetime.utcnow())


@playground_bp.route('/flash', methods=['GET'])
def show_flash():
    flash(u'Invalid password provided', 'error')
    return render_template('playground/flash.html')


@playground_bp.route('/jinja', methods=['GET'])
def test_jinja():
    flash(u'Invalid password provided', 'error')
    return render_template('playground/jinja.html')
