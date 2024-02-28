n, m = tuple(map(int, input().split()))
graph = [
    [0]*n
    for _ in range(n)
]
visited = [0]*n
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    graph[a-1][b-1] = 1

def dfs(node):
    node = node - 1
    for curr_v in range(n):
        if graph[node][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)
cnt = 0
for v in visited:
    if v:
        cnt += 1
print(cnt)