#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This is a Calculator App
"""
    Calculator App with Basic and Adv functions
"""
import sys

from calculator.app.basic import *
from calculator.app.adv import *

def main():
    while True:
        menu = """
            Menu Options
            ------------
            1. Basic Calc Examples
            2. Adv Calc Examples
            q. Quit
        """

        print("********** CALC APP **********")
        print(menu)
        option = input("Enter option: 1-2, q=quit: ")

        if option == "1":
            print(f"9 * 8 * 7 = {add(9, 8, 7)}")
            print(f"9 * 8 * 7 = {mul(9, 8, 7)}")
            print(f"9 / 8 = {div(9, 8)}")
        elif option == "2":
            print(f"9 % 8  = {mod(9, 8)}")
            print(f"9**8 = {power(9, 8)}")
            print(f"\N{square root}98 = {sqrt(98)}")
        elif option == "q":
            break
    return None

# Namespace Trick
if __name__ == "__main__":
    # EXECUTE ONLY if ran directly as a program
    # Ignored if imported as a module
    main()
    sys.exit(0)