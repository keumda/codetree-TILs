from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

q = deque()

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] == 0:
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
            # print(new_x, new_y)
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append([new_x, new_y])

visited[0][0] = True
q.append([0, 0])
bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)