from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key = app.config.get('SECRET_KEY')
migrate = Migrate(app, db)
Bootstrap(app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)

from app import views, models, commands
