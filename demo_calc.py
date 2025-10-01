#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""

def add(*args):
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    total = 1
    for num in args:
        total *= num
    return float(total)

l_div = lambda x, z: round(x/z, 3)
print(f"5/4 = {l_div(5, 4)}")