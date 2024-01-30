n = int(input())

offset = 10
slots = [0]*2001
start_idx = 1000
for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)
    if direction == 'L':
        for i in range(start_idx-x, start_idx):
            slots[i] += 1
        start_idx -= x
        # print(slots[985:1005])
    if direction == 'R':
        for i in range(start_idx, start_idx+x):
            slots[i] += 1
        start_idx += x
        # print(slots[985:1005])
    
twice_cnt = 0
# print(slots[985:1005])
for elem in slots:
    if elem >= 2:
        twice_cnt += 1
print(twice_cnt)