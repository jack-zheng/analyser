from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required, current_user

from app.models import Admin
from app.forms import LoginForm
from app.utils import redirect_back


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('history.hello'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            if admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Incorrect password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()
