from datetime import datetime
from ./../project.models import TestCase

def generate_case(record):
    create_date = datetime.fromtimestamp(int(record[3]))
    last_update = datetime.fromtimestamp(int(record[5]))
    tmp = TestCase(file_name=record[1], author=record[2], create_date=create_date, last_update_by=record[4], last_update_time=last_update, file_path=record[6])
    return tmp


