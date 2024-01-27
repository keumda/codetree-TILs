n = int(input())

arr = []
for _ in range(n):
    data = tuple(input().split())
    arr.append(data)

min_date = 2100
rainy_date = ('', '', '')
for elem in arr:
    if elem[2] == 'Rain':
        if min_date > int(elem[0][:4]):
            min_date = int(elem[0][:4])
            rainy_date = elem

print(rainy_date[0], rainy_date[1], rainy_date[2])