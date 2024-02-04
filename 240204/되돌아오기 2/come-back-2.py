command = input()

x, y = 0, 0
t = 0
res = -1
d = ['N', 'E', 'S', 'W']
d_idx = 0
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
for c in command:
    if c == 'R':
        d_idx = (d_idx + 1) % 4
    if c == 'L':
        # 그 다음 dir_num을 (dir_num + 3) % 4로 설정하는 것이 좋습니다.
        d_idx = (d_idx - 1 + 4) % 4
    if c == 'F':
        x, y = x + dx[d_idx], y + dy[d_idx]
    # print(c, x, y, d_idx, d[d_idx])
    t += 1
    if x == 0 and y == 0:
        res = t
        break
print(res)