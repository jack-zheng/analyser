from flask import Flask
from config import Config
from elasticsearch import Elasticsearch


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    print(app.config['ESSEARCH_URL'])
    app.elasticsearch = Elasticsearch([app.config['ESSEARCH_URL']])

    from .admin.admin_module import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from .essearch.search import essearch_bp
    app.register_blueprint(essearch_bp, url_prefix='/essearch')

    from .core.core import core_bp
    app.register_blueprint(core_bp)

    return app