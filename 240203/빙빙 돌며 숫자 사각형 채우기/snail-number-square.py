n, m = tuple(map(int, input().split()))
visted = [
    [0] * m
    for _ in range(n)
]

def in_range(r, c):
    if r >= 0 and c >= 0 and r < n and c < m:
        return visted[r][c] == 0
    else:
        return False

st_n = 1
dis, djs = [0, 1, 0, -1], [1, 0, -1, 0]
d = 0
i_idx, j_idx = 0, 0

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            visted[i][j] = st_n
            continue
        if not in_range(i_idx + dis[d], j_idx + djs[d]):
            d = (d + 1) % 4
        i_idx, j_idx = i_idx + dis[d], j_idx + djs[d]
        st_n += 1
        # print(i_idx, j_idx, st_n)
        visted[i_idx][j_idx] = st_n

for row in visted:
    for elem in row:
        print(elem, end=' ')
    print()