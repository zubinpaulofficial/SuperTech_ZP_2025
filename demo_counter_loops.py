#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will how to repeat a block of commands a specific number of times using a counter loop.
"""
    Docstring:
"""

count = 0 # Initialise counter
while count < 10: # Test condition
    print(count)
    count += 1 # Increment/Decrement counter

# Alternatively, could use a for loop and built in 'range(start, stop, step)' function

for num in range(0, 10, 1):
    print(num)

# built in 'range(start, stop, step)'
for num in range(0, 10):
    print(num)

for num in range(10):
    print(num)