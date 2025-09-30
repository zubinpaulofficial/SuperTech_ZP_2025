#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# a)	A line of hyphens the same length as the Belgium string
print("-" * len(Belgium))

# b)	The string with the comma separators replaced by colons ':'.
print(Belgium.replace(",",":"))

# c)	The population of Belgium (the second field) plus the population of the capital city (the fourth field).
# Hint: the answer should be 11183818.
fields = Belgium.split(",")
total_population = int(fields[1]) + int(fields[3])
print(total_population)