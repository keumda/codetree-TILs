def fill_rect(x, y, x1, y1, num):
    for i in range(y, y1):
        for j in range(x, x1):
            arr[i][j] = num

arr = [[0 for j in range(2000)] for i in range(2000)]
offset = 1000
for i in range(2):
    x, y, x1, y1 = tuple(map(int, input().split()))
    fill_rect(x+offset, y+offset, x1+offset, y1+offset, 1)
x, y, x1, y1 = tuple(map(int, input().split()))
fill_rect(x+offset, y+offset, x1+offset, y1+offset, 0)

res = 0
for row in arr:
    for elem in row:
        if elem == 1:
            res += 1
print(res)