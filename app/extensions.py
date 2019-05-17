from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment


db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
moment = Moment()
