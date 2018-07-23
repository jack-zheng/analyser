from config import Config
import unittest
from app import create_app

class Test_Config(Config):
    DEBUG=1


class Tests(unittest.TestCase):

    def setUp(self):
        print("SETUP")
        self.app = create_app(Test_Config)

    def tearDown(self):
        print("TEARDOWN")

    def test_config(self):
        self.assertEqual(1, self.app.config['DEBUG'])

if __name__ == '__main__':
    unittest.main()