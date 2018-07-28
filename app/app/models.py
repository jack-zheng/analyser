from datetime import datetime


class TestCase(object):
    def __init__(self, file_name=None, author=None, 
        create_date=None, 
        last_update_by=None, 
        last_update_time=None, file_path=None):
        self.file_name = file_name
        self.author = author
        self.create_date = create_date
        self.last_update_by = last_update_by
        self.last_update_time = last_update_time
        self.file_path = file_path
    
    def __repr__(self):
        return '<Case: name=%r, author=%r>' % (self.file_name, self.author)