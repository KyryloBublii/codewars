import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def basic_test_cases(self):
        self.assert_equals( digital_root(16), 7, "digital_root(16)")
        self.assert_equals( digital_root(942), 6, "digital_root(942)")
        self.assert_equals( digital_root(132189), 6, "digital_root(132189)")
        self.assert_equals( digital_root(493193), 2, "digital_root(493193)")

if __name__ == '__main__':
    unittest.main()
