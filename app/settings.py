import os
import sys


basedir = os.path.abspath(os.path.dirname(__file__))

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    member_count_per_page = os.getenv('member_count_per_page', '8')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_ENABLE_CSRF = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_ENABLED = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'dev.db')
    WTF_CSRF_CHECK_DEFAULT = False


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', prefix + os.path.join(basedir, 'app.db'))
    DEBUG_TB_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
