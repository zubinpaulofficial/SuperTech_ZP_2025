#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""
def say_hello(greeting, recipient):
    message = greeting + " " + recipient
    print(message)

say_hello("Hello", "Zubin")
say_hello(greeting="Hello", recipient="Zubin")



def say_hello2(*, greeting, recipient): #ENFORCED
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello(greeting="Hello", recipient="Zubin")