def fill_rect(x, y, x1, y1):
    for i in range(y, y1):
        for j in range(x, x1):
            arr[i][j] = 1

n = int(input())

arr = [[0 for j in range(200)] for i in range(200)]
offset = 100
for _ in range(n):
    x, y, x1, y1 = tuple(map(int, input().split()))
    fill_rect(x+100, y+100, x1+100, y1+100)

res = 0
for row in arr:
    for elem in row:
        if elem == 1:
            res += 1
print(res)