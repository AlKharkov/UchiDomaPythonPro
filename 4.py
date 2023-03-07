import datetime

day, month, year = map(int, input().split('.'))
date = datetime.date(year, month, day)
delta = datetime.timedelta(days=1)
counter = 0
while date.month == month:
    print(date.strftime('%d.%m.%Y'), 'рабочий' if counter % 4 < 2 else 'выходной')
    counter += 1
    date += delta
