#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will simulate a high street bank ATM machine
"""
    Docstring:
"""

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid Pin")
        break
    else:
        print("Invalid Pin")
        attempts += 1
else:
    # ONLY executes if WHILE LOOP becomes FALSE
    print("Too many attempts")
    print("Your card has been retained. Have a nice day!")

print("Done")