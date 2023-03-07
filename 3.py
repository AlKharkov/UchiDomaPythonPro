import datetime

current = int(input())
day, month, year = map(int, input().split('.'))
date = datetime.date(year, month, day)
delta = datetime.timedelta(days=1)
ans = list()
while len(ans) < 4:
    if current < 3:
        if date.day % 2 == 0:
            if date.weekday() > 4:
                ans.append(date.strftime('%d.%m.%Y'))
                current += 1
    date += delta
    if date.month != month:
        current = 0
        month = date.month
for i in ans:
    print(i)
