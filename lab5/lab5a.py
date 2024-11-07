#!/usr/bin/env python3

def read_file_string(filename):
    """Reads the entire file as a single string."""
    with open(filename, 'r') as file:
        content = file.read()
    return content

def read_file_list(filename):
    """Reads the file line by line and returns a list of lines without newline characters."""
    with open(filename, 'r') as file:
        content = [line.strip() for line in file]
    return content
