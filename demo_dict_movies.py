#! /usr/bin/env python3
# Author: Zubin Paul
# Description: This script will demo
"""
    Docstring:
"""
import pprint

movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
        'charles': ['puss in boots', 'the last wish', 'django unchained'],
        'diren': ['top gun', 'wolf of wall street', 'rio'],
}

movies['donald'] = ['lotr', 'the hobbit', 'star wars']
pprint.pprint(movies)

print("-" * 60)

movies.pop('charles') #removes key + value
movies.popitem() #removes the LAST ONE INSERTED

print(f"Kymran's fav three movies are: {movies['kymran']}")

print("-" * 60)

print(f"Kymran's ultimate film is: {movies['kymran'][0]}")

#GET
print(f"Kymran's fav three movies are: {movies.get('kymran')}")
print(f"Kymran's ultimate film is: {movies.get('kymran')[0]}")

#COPY
# films = movies.copy()
# # films.clear()
# pprint.pprint(films)

for films in movies.values():
    print(f"Good films = {films}")

for (name, films) in movies.items():
    print(f"{name} LOVES the films {films}")