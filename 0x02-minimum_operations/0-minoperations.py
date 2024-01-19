#!/usr/bin/python3
""" method that calculates the fewest number of operations
needed to result in exactly n H characters in the file."""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    str = 'H'
    operations = 0
    factor = 2
    if n < 0:
        return 0

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
