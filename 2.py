import datetime

month, year = map(int, input().split())
print('пн\tвт\tср\tчт\tпт\tсб\tвс\t')
date = datetime.date(year, month, 1)
delta = datetime.timedelta(days=1)
week = ['' for _ in range(7)]
while date.month == month:
    week[date.weekday()] = str(date.day)
    if date.weekday() == 6:
        print('\t'.join(week) + '\t')
        week = ['' for _ in range(7)]
    date += delta
for day in week:
    if day:
        print(day, end='\t')
if week.count('') != 7:
    print()
