import json
# 4.16
with open('weather.json') as file:
    data = json.load(file)
    print(max([i['main']['temp_max'] for i in data['list']]))
