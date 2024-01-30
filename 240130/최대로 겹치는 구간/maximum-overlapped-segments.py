n = int(input())

offset = 100
slots = [0]*200
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    x += 100
    y += 100
    for i in range(x, y):
        slots[i] += 1
    
max_overlap_cnt = 0
for elem in slots:
    if elem > max_overlap_cnt:
        max_overlap_cnt = elem

# print(slots)
print(max_overlap_cnt)