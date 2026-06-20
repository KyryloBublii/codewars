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


def rot13(message):
    root13in = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    root13out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    root13map = dict(zip(root13in, root13out))

    res = ''.join([root13map.get(s, s) for s in message])

    return res

def rot131(message):
    PAIRS = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))
    return "".join(PAIRS.get(c, c) for c in message)

def rot132(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)