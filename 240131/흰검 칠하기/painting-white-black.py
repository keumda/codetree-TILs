n = int(input())

slots = ['W/0/B/0/N']*200001
start_idx = 100000
for _ in range(n):
    x_str, direction = tuple(input().split())
    x = int(x_str)
    if direction == 'R':
        for i in range(start_idx, start_idx+x):
            curr = list(slots[i].split('/'))
            curr[3] = str(int(curr[3]) + 1)
            curr[4] = 'B'
            slots[i] = '/'.join(curr)
        start_idx = start_idx+x - 1
    if direction == 'L':
        for i in range(start_idx-x+1, start_idx+1):
            curr = list(slots[i].split('/'))
            curr[1] = str(int(curr[1]) + 1)
            curr[4] = 'W'
            slots[i] = '/'.join(curr)
        start_idx = start_idx-x+1

b_cnt = 0
w_cnt = 0
g_cnt = 0
for elem in slots:
    curr = tuple(elem.split('/'))
    if int(curr[3]) >= 2 and int(curr[1]) >= 2:
        g_cnt += 1
    elif curr[4] == 'B':
        b_cnt += 1
    elif curr[4] == 'W':
        w_cnt += 1

print(w_cnt, b_cnt, g_cnt)