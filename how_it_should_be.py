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

