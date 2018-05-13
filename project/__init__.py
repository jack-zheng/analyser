from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.secret_key=app.config.get('SECRET_KEY')
migrate = Migrate(app, db)

from project import views, models
