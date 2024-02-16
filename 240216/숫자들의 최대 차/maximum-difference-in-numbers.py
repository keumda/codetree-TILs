n, k = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(n)
]

max_cnt = 0
arr.sort()

for i in range(n):
    cnt = 0
    for j in range(n+1):
        if arr[i:j]:
            # print(arr[i:j])
            if max(arr[i:j]) - min(arr[i:j]) <= k:
                cnt = len(arr[i:j])
            else:
                break
    max_cnt = max(cnt, max_cnt)
print(max_cnt)