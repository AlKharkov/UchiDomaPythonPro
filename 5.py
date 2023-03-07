import datetime

day, month, year = map(int, input().split('.'))
current_date = datetime.date(year, month, day)
day, month, year = map(int, input().split('.'))
birthday_date = datetime.date(year, month, day)
delta = datetime.timedelta(days=1)
counter = 0
while current_date.month != birthday_date.month or current_date.day != birthday_date.day:
    counter += 1
    current_date += delta
print(counter)
