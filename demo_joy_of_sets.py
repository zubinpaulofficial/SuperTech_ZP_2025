#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""

marvel_fans = {"ayo", "charles", "arash", "zubin", "diren", "sage", "donald"}
dc_fans = set() #create empty set

#Add
dc_fans.add("donald")
dc_fans.add("ben")
dc_fans.add("deenesh")

#Shrink
# dc_fans.pop() #RANDOMLY REMOVE
# comic_fans = dc_fans.copy() #Copies SET
# comic_fans.clear() #empty the set

# print(f"Fans of Marvel: {marvel_fans}")
# print(f"Fans of DC: {dc_fans}")


print(f"Fans of Marvel or DC: {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC: {marvel_fans.intersection(dc_fans)}")
print(f"Fans of only Marvel : {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC: {marvel_fans.symmetric_difference(dc_fans)}")

print("-" * 60)

print(f"Fans of Marvel or DC: {marvel_fans | dc_fans}")
print(f"Fans of Marvel AND DC: {marvel_fans & dc_fans}")
print(f"Fans of only Marvel : {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel OR DC: {marvel_fans ^ dc_fans}")