n = int(input())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = sum(arr[i][j:j+3])
        # print(cnt, arr[i][j:j+3])
        if cnt > max_cnt:
            max_cnt = cnt
print(max_cnt)