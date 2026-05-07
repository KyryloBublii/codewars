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