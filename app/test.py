from config import Config
import unittest
from app import create_app
from app.essearch.search import essearch_bp
from datetime import datetime


class Test_Config(Config):
    DEBUG=1


class Tests(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Test_Config)
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_config(self):
        ret = self.client.get('/essearch/')
        self.assertEqual(ret.status_code, 200)

    def test_post_record(self):
        '''
        Test
        @endpoint /api/record
        @datatype json
        @datafields 
            file_name
            author
            create_date
            last_update_by
            last_update_time
            file_path
        '''
        record = '{"file_name": "tmp_name",\
                    "author": "jack01",\
                    "create_date": "1",\
                    "last_update_by": "jack02",\
                    "last_update_time": "2",\
                    "file_path": "/a/b/c"}'
        resp = self.client.post('/essearch/api/record', data=record, headers={"Content-type": "application/json"})
        print(resp.status_code)

if __name__ == '__main__':
    unittest.main()