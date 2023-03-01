import csv
# Yarael Poof
with open('starwars.csv') as file:
    data = csv.reader(file)
    name, maximal = 0, 0
    for line in data:
        if line[0] == 'name':
            continue
        if line[1] != 'NA':
            if maximal < int(line[1]):
                maximal = int(line[1])
                name = line[0]
    print(name)
