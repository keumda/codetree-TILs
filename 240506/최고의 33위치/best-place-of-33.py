n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_sum(grid):
    s = 0
    for row in grid:
        for item in row:
            s += item
    return s


max_cnt = 0
m = 3
for i in range(n - m + 1):
    for j in range(n - m + 1):
        s = get_sum(grid[i:i+m][j:j+m])
        max_cnt = max(max_cnt, s)

print(max_cnt)