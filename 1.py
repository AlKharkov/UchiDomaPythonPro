import datetime

day, month, year = map(int, input().split('.'))
date = datetime.date(year, month, day)
delta = datetime.timedelta(days=1)
while date.year == year:
    if date.weekday() > 4:
        print(date.strftime('%d.%m.%Y'))
    date += delta
