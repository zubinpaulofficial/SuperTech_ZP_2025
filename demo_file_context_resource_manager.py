#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""

movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
        'charles': ['puss in boots', 'the last wish', 'django unchained'],
        'diren': ['top gun', 'wolf of wall street', 'rio'],
          'donald': ['lotr', 'the hobbit', 'star wars']
}

with open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(name, movies[name])
        fh_out.write(f"{name} {movies[name]}\n")

    print('-' * 60)

    #Opening in TEXT Mode (READING)
with open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/movies.txt", mode="rt") as fh_in:
    text = fh_in.readline()
    print(text)

    print('-' * 60)

    for line in fh_in:
        print(line, end='')

    print('-' * 60)

    for line in open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/movies.txt", mode="rt"):
        print(line, end='')