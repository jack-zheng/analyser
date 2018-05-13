from project import db
from sqlalchemy import desc
from datetime import datetime


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_name = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    last_update_by = db.Column(db.String(), nullable=False)
    last_updte_time = db.Column(db.DateTime)

    @staticmethod
    def get_all():
        return TestCase.query.all()

    @staticmethod
    def get_max_id_record():
        return TestCase.query.order_by(desc(TestCase.id)).first()

    def get_case_info(self, search_key):
        return TestCase.query.filter(TestCase.file_name.like('%'+search_key+'%')).all()
    
    def __repr__(self):
        return '<Case: id=%r, name=%r, author=%r>' % (self.title, self.file_name, self.author)