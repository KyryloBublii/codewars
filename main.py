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
