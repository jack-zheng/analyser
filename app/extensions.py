from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_wtf import CSRFProtect


db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
moment = Moment()
debugToolbarExtension = DebugToolbarExtension()
login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from app.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'