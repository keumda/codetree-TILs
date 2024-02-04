import sys

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize
for i in range(n):
    total_dist = 0
    for j, h in enumerate(arr):
        cur_dist = h * abs(j - i)
        total_dist += cur_dist
        # print(h, abs(j - i), cur_dist, total_dist)
    # print('================')
    if min_dist > total_dist:
        min_dist = total_dist
print(min_dist)