n = int(input())

arr = []
for _ in range(n):
    name, h, w = tuple(input().split())
    user = (name, int(h), int(w))
    arr.append(user)
arr.sort(key=lambda x:(x[1], -x[2]))

for elem in arr:
    print(elem[0], elem[1], elem[2])