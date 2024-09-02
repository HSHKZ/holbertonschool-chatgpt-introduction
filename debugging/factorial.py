#!/usr/bin/python3

import sys

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            return result

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <number>".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv [1])
    except ValueError
        print("Error: Please provide an integer as input")
        sys.exit(1)

    print(factorial(n))

if __name__ == "__main__":
    main()
