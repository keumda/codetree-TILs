n = int(input())

slots = [0]*100
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    for i in range(x-1, y):
        slots[i] += 1

overlap_cnt = 0
for elem in slots:
    if overlap_cnt < elem:
        overlap_cnt = elem
print(overlap_cnt)