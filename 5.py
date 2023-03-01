import json
import csv
# rate.json not opened
with open('rate.json') as file:
    inlet = json.load(file, ensure_ascii=True, indent=2)['Valute']

data = sorted([[line['CharCode'], line['Name']] for line in inlet.values()])
for i in range(len(data)):
    if data[i][0] == 'USD':
        print(i + 1)
        break

with open('rate.csv', 'w', encoding='utf-8', newline='') as file:
    outlet = csv.writer(file)
    outlet.writerow(['CharCode', 'Name'])
    outlet.writerows(data)
