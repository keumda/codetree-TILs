n = int(input())
arr = []
for _ in range(n):
    name, k, e, m = tuple(input().split())
    student = (name, int(k), int(e), int(m))
    arr.append(student)
arr.sort(key=lambda x: x[1]+x[2]+x[3])

for elem in arr:
    print(elem[0], elem[1], elem[2], elem[3])