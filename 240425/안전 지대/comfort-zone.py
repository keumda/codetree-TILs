n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
after_grid = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(i, j):
    return 0 <= i and i < n and 0 <= j and j < m

def can_go(i, j):
    if not in_range(i, j):
        return False
    if visited[i][j] == 1:
        return False
    if after_grid[i][j] == 0:
        return False
    return True

def dfs(i, j):
    dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj
        if can_go(new_i, new_j):
            visited[new_i][new_j] = 1
            dfs(new_i, new_j)
    
max_k = 0
for r in grid:
    for v in r:
        max_k = max(max_k, v)

res = []
for k in range(1, max_k+1):
    for r in range(n):
        for c in range(m):
            if grid[r][c] <= k:
                after_grid[r][c] = 0
            else:
                after_grid[r][c] = 1
    visited = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if after_grid[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1
                dfs(x, y)
                cnt += 1
    res.append(cnt)
print(res.index(max(res))+1, max(res))