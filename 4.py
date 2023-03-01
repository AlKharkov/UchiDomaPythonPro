import csv
# 306
with open('ratings.csv') as file:
    data = csv.DictReader(file)
    print(len(list(filter(lambda x: 'drama' in x, [line['Genres'] for line in data]))))
