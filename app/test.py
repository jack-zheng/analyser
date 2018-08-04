from config import Config
import unittest
from app import create_app
from app.essearch import gitutil


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

    def test_git_util(self):
        gitutil.test_print()


if __name__ == '__main__':
    unittest.main()