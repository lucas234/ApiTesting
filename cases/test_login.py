# coding:utf-8
import unittest
from test_env import create_session
from api.account import AccountApi


class MyTestCase(unittest.TestCase):

    def setUp(self):
        session = create_session()
        self.account_api = AccountApi(session)

    def test_something(self):
        r = self.account_api.login("15566778800", "123456")
        self.assertEqual(r['userId'], "XXXX")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
