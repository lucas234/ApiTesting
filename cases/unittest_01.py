import unittest
from unittest import skipIf


class MyTestCase(unittest.TestCase):
    a = 10

    def test_something(self):
        print self.a+20
        self.assertEqual(True, True)

    @unittest.skipIf(a == 10, "test")
    def test_1_plus_3(self):
        print "hello"
        self.assertEqual(1 + 3, 4)

    @unittest.skip("just skip")
    def test_1_plus_4(self):
        self.assertEqual(1 + 5, 4)


if __name__ == '__main__':
    unittest.main()
