#!/usr/bin/python3
import sys

# factorial - Recursively returns factorial of a given number
def factorial(n):
    if n == 0:
        return 1  # Returns 1 for 0 factorial
    else:
        return n * factorial(n-1)  # Returns n factorial

f = factorial(int(sys.argv[1]))
print(f)