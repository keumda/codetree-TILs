n, m = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for _ in range(m)
]
max_cnt = 0
for i in range(m):
    cnt = 1
    for j in range(m):
        if i != j:
            a = [min(arr[i][0], arr[i][1]), max(arr[i][0], arr[i][1])]
            b = [min(arr[j][0], arr[j][1]), max(arr[j][0], arr[j][1])]
            if a == b:
                cnt += 1
            # print(i, a, b, cnt)
    max_cnt = max(cnt, max_cnt)
print(max_cnt)