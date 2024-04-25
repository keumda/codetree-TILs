import sys
sys.setrecursionlimit(3000)

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(i, j):
    return 0 <= i and i < n and 0 <= j and j < n

def can_go(i, j):
    global curr
    if not in_range(i, j):
        return False
    if visited[i][j] == 1:
        return False
    if grid[i][j] != curr:
        return False
    return True

def dfs(i, j):
    global cnt
    dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj
        if can_go(new_i, new_j):
            visited[new_i][new_j] = 1
            cnt += 1
            dfs(new_i, new_j)

res = [] 
for x in range(n):
    for y in range(n):
        if visited[x][y] == 0:
            curr = grid[x][y]
            cnt = 0
            visited[x][y] = 1
            cnt += 1
            dfs(x, y)
    res.append(cnt)

exploded = 0
max_cnt = 0
for c in res:
    if c >= 4:
        exploded += 1
    max_cnt = max(max_cnt, c)
print(exploded, max_cnt)