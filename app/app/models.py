from datetime import datetime


class TestCase(object):
    def __init__(self, file_name="NA", author="NA", 
        create_date=datetime.utcnow(), 
        last_update_by="NA", 
        last_update_time=datetime.utcnow(), file_path="NA"):
        self.file_name = file_name
        self.author = author
        self.create_date = create_date
        self.last_update_by = last_update_by
        self.last_update_time = last_update_time
        self.file_path = file_path
    
    def __repr__(self):
        return '<Case: name=%r, author=%r>' % (self.file_name, self.author)