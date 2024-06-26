from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
ks = [
    list(map(int, input().split()))
    for _ in range(k) 
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
q = deque()

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] == 1:
        return False
    if visited[x][y]:
        return False
    return True

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append([new_x, new_y])

for st_x, st_y in ks:
    st_x, st_y = st_x - 1, st_y - 1

    visited[st_x][st_y] = True
    q.append([st_x, st_y])
    bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1
print(cnt)