import unittest
from main import *


class TestSumTwoSmallest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]), 3453455)
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        self.assertEqual(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        self.assertEqual(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)


class TestDigitalRoot(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)
        self.assertEqual(digital_root(39512890680022105939), 1)

class TestRepeatStr(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(repeat_str(4, 'a'), 'aaaa')
        self.assertEqual(repeat_str(3, 'hello '), 'hello hello hello ')
        self.assertEqual(repeat_str(2, 'abc'), 'abcabc')
        self.assertEqual(repeat_str(0, ''), '')
        self.assertEqual(repeat_str(0, 'I'), '')
        self.assertEqual(repeat_str(5, ''), '')
        self.assertEqual(repeat_str(6, 'I'), 'IIIIII')
        self.assertEqual(repeat_str(5, 'Hello'), 'HelloHelloHelloHelloHello')

class TestDescendingOrder(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(descending_order(0), 0)
        self.assertEqual(descending_order(15), 51)
        self.assertEqual(descending_order(123456789), 987654321)


if __name__ == '__main__':
    unittest.main()
