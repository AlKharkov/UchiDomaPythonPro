import json

with open('example.json') as file:
    data = json.load(file)
    print(sum([i['value'] for i in data['clues']]))
