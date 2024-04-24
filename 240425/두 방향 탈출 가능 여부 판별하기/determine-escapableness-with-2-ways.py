n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
answer = [
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
    if grid[i][j] == 0:
        return False
    return True

def dfs(i, j):
    dis, djs = [1, 0], [0, 1]
    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj

        if can_go(new_i, new_j):
            visited[new_i][new_j] = 1
            dfs(new_i, new_j)

dfs(0, 0)
print(visited[n-1][m-1])