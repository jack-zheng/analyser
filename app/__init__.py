from flask import Flask, render_template
from app.settings import config

import click
import os
from dotenv import load_dotenv
from app.models import TestCase, User, CaseBackup

from app.blueprints.member import member_bp
from app.blueprints.history import history_bp
from app.blueprints.playground import playground_bp
from app.blueprints.auth import auth_bp

from app.extensions import bootstrap, migrate, db, moment,\
     debugToolbarExtension, login_manager, csrf


load_dotenv()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('app')
    app.config.from_object(config[config_name])
    app.secret_key = app.config.get('SECRET_KEY')
    register_extensions(app)
    register_blueprints(app)
    register_shell_context(app)
    register_commands(app)
    register_errors(app)
    return app


def register_blueprints(app):
    app.register_blueprint(history_bp)
    app.register_blueprint(member_bp, url_prefix='/member')
    app.register_blueprint(playground_bp, url_prefix='/playground')
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_extensions(app):
    bootstrap.init_app(app)
    migrate.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    debugToolbarExtension.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Drop tables and create.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, \
                do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    @click.option(
        '--count', default=20, help='Quantity of data, default is 20.')
    def forge(count):
        """Generate fake data."""
        from faker import Faker

        db.drop_all()
        db.create_all()

        fake = Faker()

        click.echo('Create fake data in test_case table...')
        for i in range(count):
            message = TestCase(
                file_name="fakename" + str(i),
                author=fake.name(),
                create_date=fake.date_time(),
                last_update_by=fake.name(),
                last_update_time=fake.date_time_this_year(),
                file_path="filepath" + str(i)
            )
            db.session.add(message)
        db.session.commit()

        click.echo('Create fake data in user table...')
        for i in range(count):
            message = User(
                id='tmpid' + str(i),
                username=fake.name(),
                email=fake.email()
            )
            db.session.add(message)

        db.session.commit()
        click.echo('Created %d fake record in each table.' % count)

    @app.cli.command()
    def recover_svn():
        """Extract data from sql file and insert to case_backup table."""
        click.echo('Clean Case Backup Table')
        CaseBackup.query.delete()
        db.session.commit()

        click.echo('Start Recover...')
        sql_file = 'case_backup.sql'
        with open(sql_file, 'r') as file:
            for sql in file.readlines():
                db.engine.execute(sql)
        click.echo('Finish Data Recover...')
