n = int(input())
arr = []
for i in range(n):
    h, w = tuple(map(int, input().split()))
    student = (h, w, i+1)
    arr.append(student)
arr.sort(key=lambda x:(x[0], -x[1]))

for elem in arr:
    print(elem[0], elem[1], elem[2])