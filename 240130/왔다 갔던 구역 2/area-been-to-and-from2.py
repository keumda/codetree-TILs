n = int(input())

offset = 10
slots = [0]*2001
start_idx = 1000
for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)
    if direction == 'L':
        for i in range(start_idx-1, start_idx-x-1, -1):
            slots[i] += 1
        start_idx -= x
    if direction == 'R':
        for i in range(start_idx, start_idx+x):
            slots[i] += 1
        start_idx += x
    
twice_cnt = 0
for elem in slots:
    if elem >= 2:
        twice_cnt += 1
print(twice_cnt)


# for i in range(2, 5):
#     print(i, end=' ')
# print()
# for j in range(5-1, 2-1, -1):
#     print(j, end=' ')