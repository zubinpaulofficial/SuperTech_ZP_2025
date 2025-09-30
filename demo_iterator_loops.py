#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""
import sys

heroes = ['JFK', 'marie antoinette', 'm.jackson', 'ozzie', 'pele',
          'malcom X', 'kobe', 'diana']

# for name in heroes:
#     print(name)
#
# idx = 0
# for name in heroes:
#     print(name.upper(), end="\n")
#     heroes[idx].upper()
#     idx += 1
# print("Heroes =", heroes)

idx = 0
for (idx, name) in enumerate(heroes):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
    idx += 1
print("Heroes =", heroes)

try:
    sys.exit(0) # Explicit EXIT with "expression" -> STDERR (red)
    # + return code (0=success, 1-255=error code)
except SystemExit:
    print("Quitting")