arr = []

for _ in range(5):
    name, h, w = tuple(input().split())
    user = (name, int(h), float(w))
    arr.append(user)

arr.sort(key=lambda x:x[0])
print('name')
for elem in arr:
    print(elem[0], elem[1], elem[2])
print()
print('height')
arr.sort(key=lambda x:-x[1])
for elem in arr:
    print(elem[0], elem[1], elem[2])