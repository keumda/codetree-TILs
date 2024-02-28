n, m = tuple(map(int, input().split()))
graph = [
    [0]*(n+1)
    for _ in range(n+1)
]
visited = [0]*(n+1)
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)
def dfs(node):
    for curr_v in range(1, n+1):
        if graph[node][curr_v] and not visited[curr_v]:
            # print(curr_v)
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)
# print(visited)

cnt = 0
for v in visited:
    if v:
        cnt += 1
print(cnt-1)