n, t = tuple(map(int, input().split()))
r, c, d = tuple(input().split())

r, c = int(r)-1, int(c)-1
di, dj = [0, -1, 1, 0], [1, 0, 0, -1]
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3,
}

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

d_idx = mapper[d]
for sec in range(t):
    nr, nc = r + di[d_idx], c + dj[d_idx]
    # print(d_idx, r, c, nr, nc)
    if not in_range(nr, nc):
        d_idx = 3 - d_idx
        # print('here', d_idx)
    else:
        r, c = nr, nc

print(r+1, c+1)