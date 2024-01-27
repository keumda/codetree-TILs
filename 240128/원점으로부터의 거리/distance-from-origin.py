n = int(input())
arr = []
for i in range(n):
    x, y = tuple(input().split())
    pt = (int(x), int(y), i+1)
    arr.append(pt)
arr.sort(key=lambda x:abs(0-x[0])+abs(0-x[1]))

for elem in arr:
    print(elem[2])