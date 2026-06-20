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


class TestXO(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(xo("ooxx"),    True)
        self.assertEqual(xo("xooxx"),   False)
        self.assertEqual(xo("ooxXm"),   True)   # case-insensitive
        self.assertEqual(xo("zpzpzpp"), True)   # no x/o present → equal counts
        self.assertEqual(xo("zzoo"),    False)
        self.assertEqual(xo("oxOx"),    True)
        self.assertEqual(xo(""),        True)   # empty string


class TestRemoveChar(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')
        self.assertEqual(remove_char('ooopsss'), 'oopss')


class TestArrayDiff(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(array_diff([1,2], [1]), [2])
        self.assertEqual(array_diff([1,2,2], [1]), [2,2])
        self.assertEqual(array_diff([1,2,2], [2]), [1])
        self.assertEqual(array_diff([1,2,2], []), [1,2,2])
        self.assertEqual(array_diff([], [1,2]), [])
        self.assertEqual(array_diff([1,2,3], [1,2]), [3])


class TestToCamelCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(to_camel_case(""), "", "An empty string was provided but not returned")
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEqual(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")


class TestIncrementString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string("fo99obar99"), "fo99obar100")
        self.assertEqual(increment_string(""), "1")


class TestIsSquare(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        self.assertEqual(is_square( 0), True,  "0 is a square number (0 * 0)")
        self.assertEqual(is_square( 3), False, "3 is not a square number")
        self.assertEqual(is_square( 4), True,  "4 is a square number (2 * 2)")
        self.assertEqual(is_square(25), True,  "25 is a square number (5 * 5)")
        self.assertEqual(is_square(26), False, "26 is not a square number")


class TestListSquared(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(1, 1), [[1, 1]])
        self.assertEqual(list_squared(2, 5), [])


if __name__ == '__main__':
    unittest.main()
