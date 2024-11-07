#!/usr/bin/env python3
# Author ID: [seneca_id]

import os

def add(number1, number2):
    """Add two numbers together, return the result, if error return string 'error: could not add numbers'."""
    try:
        # Try to convert both inputs to numbers if they are not already integers
        number1 = float(number1)
        number2 = float(number2)
        return number1 + number2
    except (ValueError, TypeError):
        return 'error: could not add numbers'


def read_file(filename):
    """Read a file, return a list of all lines, if error return string 'error: could not read file'."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError):
        return 'error: could not read file'


if __name__ == '__main__':
    # Test cases
    print(add(10, 5))                        # works
    print(add('10', 5))                      # works
    print(add('abc', 5))                     # exception
    print(read_file('seneca2.txt'))          # works
    print(read_file('file10000.txt'))        # exception