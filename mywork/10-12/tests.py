import unittest
from day1 import hello_name

class TestHello(unittest.TestCase):

    def test_hello_name(self):
        self.assertEqual(hello_name('bob'), 'hello boo')

if __name__ == "__main__":
    unittest.main()

