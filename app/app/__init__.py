from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    print(Config.ADMINS)

    from .admin.admin_module import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from .core.core import core_bp
    app.register_blueprint(core_bp)

    return app