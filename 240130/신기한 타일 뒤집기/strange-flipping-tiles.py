n = int(input())

slots = ['N']*100000
start_idx = 50000
for _ in range(n):
    x_str, direction = tuple(input().split())
    x = int(x_str)
    if direction == 'R':
        for i in range(start_idx, start_idx+x):
            slots[i] = 'B'
        start_idx = start_idx + x - 1
    if direction == 'L':
        for i in range(start_idx-1, start_idx-x-1, -1):
            slots[i] = 'W'
        start_idx = start_idx - x\

b_cnt = 0
w_cnt = 0
for elem in slots:
    if elem == 'B':
        b_cnt += 1
    if elem == 'W':
        w_cnt += 1

print(w_cnt, b_cnt)