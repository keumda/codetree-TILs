dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cur_d_idx = 0
x, y = 0, 0

path = input()
for i in path:
    if i == 'L':
        cur_d_idx -= 1
    if i == 'R':
        cur_d_idx += 1
    if i == 'F':
        idx = cur_d_idx % 4
        x, y = x + dx[cur_d_idx], y + dy[cur_d_idx]
print(x, y)