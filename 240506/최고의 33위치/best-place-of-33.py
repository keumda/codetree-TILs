n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
m = 3

def get_sum(i, j):
    s = 0
    for x in range(i, i+m):
        for y in range(j, j+m):
            s += grid[x][y]
    return s


max_cnt = 0
for i in range(n - m + 1):
    for j in range(n - m + 1):
        s = get_sum(i, j)
        max_cnt = max(max_cnt, s)

print(max_cnt)
# get_sum(0, 0)