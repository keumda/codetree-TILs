def fill_rect(x, y, x1, y1, color):
    # print(x, y, x1, y1)
    for i in range(y, y1):
        for j in range(x, x1):
            arr[i][j] = color

n = int(input())
arr = [['N' for j in range(200)] for i in range(200)]
offset = 100

for i in range(1, n+1):
    x, y, x1, y1 = tuple(map(int, input().split()))
    if i%2 == 1:
        fill_rect(x+offset, y+offset, x1+offset, y1+offset, 'R')
    else:
        fill_rect(x+offset, y+offset, x1+offset, y1+offset, 'B')

res = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 'B':
            res += 1
print(res)