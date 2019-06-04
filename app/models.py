from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(180))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String())
    author = db.Column(db.String())
    create_date = db.Column(db.DateTime)
    last_update_by = db.Column(db.String())
    last_update_time = db.Column(db.DateTime)
    file_path = db.Column(db.String())

    @staticmethod
    def get_all():
        return TestCase.query.all()

    def get_case_info(search_key):
        return TestCase.query.filter(
            TestCase.file_name.like('%'+search_key+'%')).all()

    def __repr__(self):
        return '<Case: id=%r, name=%r, author=%r, path=%r>' % (
            self.id, self.file_name, self.author, self.file_path)


class User(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<User {}, {}>'.format(self.id, self.email)


class CaseBackup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String())
    author = db.Column(db.String())
    create_date = db.Column(db.DateTime)
    last_update_by = db.Column(db.String())
    last_update_time = db.Column(db.DateTime)
    file_path = db.Column(db.String())

    def __repr__(self):
        return '<CaseBackup {}, {}>'.format(self.id, self.email)


class JobHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<JobHistory {}, {}>'.format(self.id, self.timestamp)