import json

with open('starwars.json') as file:
    data = json.load(file)
    char = list()
    for film in data['results']:
        char.extend(film['characters'])
    print(len(set(char)))
