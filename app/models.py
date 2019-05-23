from app.extensions import db


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
