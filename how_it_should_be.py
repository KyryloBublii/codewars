def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

def double_char(s):
    return ''.join(c * 2 for c in s)

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def remove_char(s):
    return s[1 : -1]

remove_char1 = lambda s: s[1:-1]


def array_diff(a: list, b: list):
    set_b = set(b)
    return [item for item in a if item not in set_b]

def array_diff1(a, b):
    return [x for x in a if x not in b]


def solution(s: str):
    return "".join(" " + c if c.isupper() else c for c in s)