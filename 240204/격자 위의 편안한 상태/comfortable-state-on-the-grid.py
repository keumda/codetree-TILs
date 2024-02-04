n, m = tuple(map(int, input().split()))
arr = [
    [0]*n for row in range(n)
]

dis, djs = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(i, j):
    return i >= 0 and j >= 0 and i < n and j < n

def is_comfortable(i, j):
    cnt = 0
    for idx in range(len(dis)):
        di, dj = dis[idx], djs[idx]
        ndi, ndj = i + di, j + dj
        if in_range(ndi, ndj) and arr[ndi][ndj] == 1:
            cnt += 1
    if cnt == 3:
        return True
    else:
        return False

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    i = r - 1
    j = c - 1
    arr[i][j] = 1
    if is_comfortable(i, j):
        print(1)
    else:
        print(0)