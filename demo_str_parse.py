#! /usr/bin/env python3
# Author: Zubin Paul and Ben Lawson
# Description: This script will demo
"""
    Docstring:
"""

with open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/words.txt", mode="rt") as fh_in:
    for line_num, line in enumerate(fh_in):
        word = line.strip()
        if word.startswith('Y') and word.endswith('n'):
            print(f"Line Number: {line_num}, Word stars with Y and ends with n: {word.upper()}")
        if 'town' in word:
            print(f"Word has 'town': {word}")