n, m = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))


max_s = 0
for i in range(n):
    s = arr[i]
    next_idx = arr[i]
    for j in range(m-1):
        v = arr[next_idx-1]
        next_idx = v
        s += v
    max_s = max(max_s, s)
print(max_s)