arr = [
    list(input())
    for _ in range(10)
]
# print(arr)

lx,ly = 0,0
rx, ry = 0, 0
bx, by = 0,0
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'L':
            lx, ly = i, j
        if arr[i][j] == 'R':
            rx, ry = i, j
        if arr[i][j] == 'B':
            bx, by = i, j


dist = abs(lx - bx) + abs(ly - by) - 1
if lx == bx and bx == rx and ((by > ry and ry > ly) or (by < ry and ry < ly)):
    dist += 2
if ly == by and by == ry and ((bx > rx and rx > lx) or (bx < rx and rx < lx)):
    dist += 2
print(dist)