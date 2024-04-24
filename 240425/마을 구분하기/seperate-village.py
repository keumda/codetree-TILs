n = int(input())

# wall = 0, ppl = 1
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
res = []

def in_range(i, j):
    return 0 <= i and i < n and 0 <= j and j < n

def can_go(i, j):
    if not in_range(i, j):
        return False
    if visited[i][j] == 1:
        return False
    if grid[i][j] == 0:
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
    

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            visited[i][j] = 1
            cnt += 1
            dfs(i, j)
            res.append(cnt)
print(len(res))
res.sort()
for p in res:
    print(p)