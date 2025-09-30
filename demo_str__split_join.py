#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""

line = "root:x:0:0:The Super User:/root:/bin/bash" # Immuatable

fields = line.split(":") # Mutable
fields[4] = "The Administrator"
fields[6] = "/bin/zsh"

line = ":".join(fields)
print("Modified string =", line)