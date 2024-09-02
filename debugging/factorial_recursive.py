#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Function Description:
    This function computes the factorial of the input integer `n` recursively.
    The factorial of a non-negative integer `n` is defined as:
    n! = n * (n-1) * (n-2) * ... * 1
    with the special case that 0! = 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the integer from the command-line argument
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)
