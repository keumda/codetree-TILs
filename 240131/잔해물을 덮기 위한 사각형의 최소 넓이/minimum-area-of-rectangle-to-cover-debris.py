def fill_rect(x, y, x1, y1, num):
    for i in range(y, y1):
        for j in range(x, x1):
            arr[i][j] = num

arr = [[0 for j in range(2000)] for i in range(2000)]
offset = 1000

x, y, x1, y1 = tuple(map(int, input().split()))
fill_rect(x+offset, y+offset, x1+offset, y1+offset, 1)
x2, y2, x3, y3 = tuple(map(int, input().split()))
fill_rect(x2+offset, y2+offset, x3+offset, y3+offset, 0)

min_x, min_y = 2001, 2001
max_x, max_y = 0, 0
area = 0
for i in range(y+offset, y1+offset):
    for j in range(+offset, x1+offset):
        if arr[i][j] == 1:
            # print(i, j)
            area+= 1
            if i <= min_y:
                min_y = i
            if j <= min_x:
                min_x = j
            if i >= max_y:
                max_y = i
            if j >= max_x:
                max_x = j

# print(arr[min_y][min_x], arr[max_y][min_x], arr[max_y][max_x], arr[min_y][max_x]) 
# print(min_x, max_x, min_y, max_y, area)

# for i in range(990, 1005):
#     for j in range(1000, 1010):
#         print(arr[i][j], end=' ')
#     print()

width = max_x - min_x + 1
height = max_y - min_y + 1

if area != 0:
    print(width * height)
else:
    print(0)