#!  /usr/bin/env python3 SHEBANG LINE (Indicates the interpreter that runs)
# Author: Zubin
# Version: 1.0
# Description: First Script!

"""
    DOCSTRING: This is a multi line comment.
"""

# name = "Donald Cameron"
name = input("Enter your name: ")

print("My name is", name, sep=" ")
print("My name is " + name)

import math
print("Cosine of 0.5 =", math.cos(0.5))

import random
print("My lucky number is", random.randint(1, 50))

print ("Done")
