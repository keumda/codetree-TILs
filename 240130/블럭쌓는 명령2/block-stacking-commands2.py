n, k = tuple(map(int, input().split()))

slot = [0]*n
for _ in range(k):
    a, b = tuple(map(int, input().split()))
    for i in range(a-1, b):
        slot[i] += 1

max_block_cnt = 0
for elem in slot:
    if elem > max_block_cnt:
        max_block_cnt = elem

# print(slot)
print(max_block_cnt)