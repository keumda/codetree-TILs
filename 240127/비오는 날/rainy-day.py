from datetime import datetime

n = int(input())

arr = []
for _ in range(n):
    data = tuple(input().split())
    arr.append(data)

rainy_day = ('2100-12-31', '', '')
for elem in arr:
    if elem[2] == 'Rain':
        date = datetime.strptime(elem[0], '%Y-%m-%d').date()
        rainy_min_date = datetime.strptime(rainy_day[0], '%Y-%m-%d').date()
        if  rainy_min_date >= date:
            rainy_day = elem

print(rainy_day[0], rainy_day[1], rainy_day[2])