import sys

n = int(input())
p_arr = []
room = [0]*n
for _ in range(n):
    p_arr.append(int(input()))
p_total = sum(p_arr)
min_dist = sys.maxsize

for i in range(n):
    dist = 0
    for j in range(i, n):
        # print(p_arr[j], (j - i))
        dist += p_arr[j] * (j - i)
    for k in range(i):
        # print(p_arr[k], (n - i + k))
        dist += p_arr[k] * (n - i + k)
    # print(dist)
    min_dist = min(min_dist, dist)
print(min_dist)