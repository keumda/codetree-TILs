n = int(input())
arr = []
for _ in range(n):
    s = tuple(input().split())
    arr.append(s)
arr.sort(key = lambda x:x[1])

for elem in arr:
    print(elem[0], elem[1], elem[2])