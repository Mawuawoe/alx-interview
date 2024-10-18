#!/usr/bin/python3
"""
A function that apply prime factoriazation
"""


def minOperations(n):
    """
    return the sum of the prime fact.
    that rep the num of operations
    """
    if n <= 1:
        return 0

    operations = 0
    divider = 2

    while n > 1:
        while n % divider == 0:
            operations += divider
            n //= divider
        divider += 1

    return operations
