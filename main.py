import re
import string
from os import pread
import math
from os.path import split


def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))

    return n

"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_two_smallest_numbers(numbers):
    min_values = []

    for _ in range(2):
        minimum = min(numbers)
        min_values.append(minimum)
        numbers.remove(minimum)

    return sum(min_values)


def positive_sum(arr):
    return sum(n for n in arr if n > 0)

'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
'''

def double_char(s):
    res = ''

    for c in s:
        res+=c*2

    return res

def repeat_str(repeat, string):
    return string*repeat


def find_average(numbers):
    # if len(numbers) == 0: return 0
    #
    # sum = 0
    #
    # for n in numbers:
    #     sum += n
    #
    # return sum / len(numbers)

    return (sum(numbers) / len(numbers)) if len(numbers) else 0

def descending_order(num):
    numbers = list(str(num))

    res = "".join(sorted(numbers)[::-1])

    return int(res)


def xo(string:str) -> bool:
    return string.lower().count('x') == string.lower().count('o')

def remove_char(s: str):
    return s[1:len(s)-1]

'''
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
'''

def array_diff(a:list, b:list):
    c =[]
    set_b = set(b)

    for item in a:
        if item not in set_b:
            c.append(item)

    return c

'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

def solution(s:str):
    res = ""
    for char in s:
        if char.isupper():
            res = res + " " + char
        else:
            res = res + char

    return res

def to_camel_case(test):
    words = re.split(r'[-_]', test)
    return words[0] + "".join(w[0].upper() + w[1:] for w in words[1:])

def increment_string(string):
    num = re.match(r"^(.*?)(\d+)$", string)

    if num:
        prefix, suffix = num.group(1), num.group(2)
        return prefix + str(int(suffix) + 1).zfill(len(suffix))
    else:
        return string + "1"

"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""

def bool_to_word(boolean):
    return "Yes" if boolean else "No"


"""
A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""

def is_square(n):
    return math.sqrt(n).is_integer() if n >= 0 else False

def reverse_words(text):
    split = text.split(' ')

    return  ' '.join(t[::-1] for t in split)

class RomanNumerals:
    dict_roma = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    @staticmethod
    def to_roman(val : int) -> str:
        ar = RomanNumerals.dict_roma[val]

        return ''

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0


def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]

    result = []

    for char in s:
        remaining = s.replace(char, '', 1)
        perm = permutations(remaining)
        for p in perm:
            result.append(char + p)

    return list(set(result))



rot13_map = {
    'A' : 'N',
    'B' : 'O',
    'C' : 'P',
    'D' : 'Q',
    'E' : 'R',
    'F' : 'S',
    'G' : 'T',
    'H' : 'U',
    'I' : 'V',
    'J' : 'W',
    'K' : 'X',
    'L' : 'Y',
    'M' : 'Z',
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z'
}


def rot13(message: str):
    result = ""

    for ch in message:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += ch

    return result


'''
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and 
then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: 
you can use dynamically allocated character strings.
'''

def list_squared(m, n) -> list:
    result = []

    for k in range(m, n + 1):
        divisors = [i for i in range(1, k + 1) if k % i == 0] # fill array with numbers that divide k
        sum_sq = sum(d * d for d in divisors) # sum of all squared divisors
        sqrt = math.isqrt(sum_sq) # gives result of square root
        if sqrt * sqrt == sum_sq: # checks if it is perfect square
            result.append([k, sum_sq])

    return result