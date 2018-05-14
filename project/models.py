from project import db
from datetime import datetime


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_name = db.Column(db.String())
    author = db.Column(db.String())
    create_date = db.Column(db.DateTime)
    last_update_by = db.Column(db.String())
    last_update_time = db.Column(db.DateTime)
    file_path = db.Column(db.String())

    @staticmethod
    def get_all():
        return TestCase.query.all()

    @staticmethod
    def get_max_id_record():
        return TestCase.query.order_by(desc(TestCase.id)).first()

    def get_case_info(self, search_key):
        return TestCase.query.filter(TestCase.file_name.like('%'+search_key+'%')).all()
    
    def __repr__(self):
        return '<Case: id=%r, name=%r, author=%r>' % (self.id, self.file_name, self.author)