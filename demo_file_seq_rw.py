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

fh_out = open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/movies.txt", mode="wt")

for name in movies.keys():
    print(name, movies[name])
    fh_out.write(f"{name} {movies[name]}\n")
fh_out.close()

print('-' * 60)

#Opening in TEXT Mode (READING)
fh_in = open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/movies.txt", mode="rt")

# text = fh_in.read() #read entire file into a str object!
text = fh_in.readline()
print(text)

print('-' * 60)

for line in fh_in:
    print(line, end='')

print('-' * 60)

for line in open(r"/Users/zpl123/Documents/Pycharm Projects/Sky_SuperTech_ZP_2025/movies.txt", mode="rt"):
    print(line, end='')

fh_in.close()

