import string


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

