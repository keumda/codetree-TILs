from collections import deque

n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(int, input().split())
r, c = r - 1, c - 1

q = deque()

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] >= limit_n:
        return False
    return True

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    global r, c
    max_n = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                if grid[new_x][new_y] > max_n:
                    max_n = grid[new_x][new_y]
                    r, c = new_x, new_y
                    # print(r, c, max_n)
                elif grid[new_x][new_y] == max_n:
                    max_n = grid[new_x][new_y]
                    if new_x < r:
                        r, c = new_x, new_y
                    elif new_x == r:
                        if new_y < c:
                            r, c = new_x, new_y
                    # print(r, c, max_n)
                q.append([new_x, new_y])

for i in range(k):
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    visited[r][c] = True
    limit_n = grid[r][c]
    q.append([r, c])
    bfs()
    # print('====', i, r, c)
    
print(r+1, c+1)