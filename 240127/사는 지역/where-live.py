n = int(input())

arr = []
for _ in range(n):
    add = tuple(input().split())
    arr.append(add)

slowest = ('a'*10, '', '')
for elem in arr:
    if elem[0] > slowest[0]:
        slowest = elem

print(f'name {slowest[0]}')
print(f'addr {slowest[1]}')
print(f'city {slowest[2]}')