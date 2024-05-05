n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0

def happy_exist(grid):
    first = grid[0]
    for item in grid:
        if first != item:
            return False
    return True

def is_happy(grid):
    # print(grid)
    for i in range(n - m + 1):        
        sub_grid = grid[i:i+m]
        if happy_exist(sub_grid):
            return True
    return False

for i in range(n):
    if is_happy(grid[i]):
        cnt += 1
for j in range(n):
    sub_grid = list()
    for k in range(n):
        sub_grid.append(grid[k][j])
    if is_happy(sub_grid):
        cnt += 1

print(cnt)