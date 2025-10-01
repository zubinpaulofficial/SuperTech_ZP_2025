#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""
def search_word(pattern="sage", *files):
    lines_matched = 0
    for file in files:
        with (open(file, mode="rt") as fh_in):
            for (line_num, line) in enumerate(fh_in, start=1):
                if line.isascii() and pattern in line:
                    print(line_num, line, end="")
                    lines_matched += 1
    return lines_matched


total_lines = 0
total_lines += search_word("arash", r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/words.txt", r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/words.txt", r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/words.txt", r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/words.txt") # DONE lines

print('-' * 60)

print(f"{total_lines} lines matched")
