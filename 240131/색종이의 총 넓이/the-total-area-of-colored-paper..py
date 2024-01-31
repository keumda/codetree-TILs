def fill_rect(x, y, x1, y1, num):
    for i in range(y, y1):
        for j in range(x, x1):
            arr[i][j] = num

n = int(input())
arr = [[0 for j in range(200)] for i in range(200)]
offset = 100
for i in range(n):
    x, y = tuple(map(int, input().split()))
    fill_rect(x+offset, y+offset, x+8+offset, y+8+offset, 1)

res = 0
for row in arr:
    for elem in row:
        if elem == 1:
            res += 1
print(res)