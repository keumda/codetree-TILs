n, k = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(n)
]

max_cnt = 0
arr.sort()

for i in range(1, n+1):
    # print(arr[:i])
    if max(arr[:i]) - min(arr[:i]) <= k:
        max_cnt = len(arr[:i])
    else:
        break
print(max_cnt)