n, t = tuple(map(int, input().split()))

commands = input()

arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

def in_range(i, j):
    return i >= 0 and j >= 0 and i < n and j < n

i, j = n // 2, n // 2
total = arr[i][j]
d_idx = 0
# print(total, arr[i][j])
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
for c in commands:
    if c == 'R':
        d_idx = (d_idx + 1) % 4
    if c == 'L':
        d_idx = (d_idx - 1 + 4) % 4
    if c == 'F':
        ni, nj = i + di[d_idx], j + dj[d_idx]
        if in_range(ni, nj):
            total += arr[ni][nj]
            i, j = ni, nj
    # print(total, c, i, j, d_idx)
print(total)