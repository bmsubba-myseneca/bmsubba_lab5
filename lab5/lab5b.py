#!/usr/bin/env python3

import os

def read_file_string(filename):
    """Reads the entire file content as a single string."""
    with open(filename, 'r') as file:
        return file.read()

def read_file_list(filename):
    """Reads the file and returns a list of lines without newline characters."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def append_file_string(filename, string):
    """Appends the given string to the file."""
    with open(filename, 'a') as file:
        file.write(string)

def write_file_list(filename, lines):
    """Writes a list of lines to a file, each on a new line."""
    with open(filename, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")

def copy_file_add_line_numbers(src_filename, dest_filename):
    """Copies content from src file to dest file, adding line numbers."""
    with open(src_filename, 'r') as src_file, open(dest_filename, 'w') as dest_file:
        for i, line in enumerate(src_file, start=1):
            dest_file.write(f"{i}:{line.strip()}\n")
