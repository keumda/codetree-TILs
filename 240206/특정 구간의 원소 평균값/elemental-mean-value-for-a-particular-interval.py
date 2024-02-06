n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        avg = sum(arr[i:j+1])//len(arr[i:j+1])
        # print(arr[i:j+1], avg)
        for k in range(i, j+1):
            if arr[k] == avg:
                cnt += 1
                break
print(cnt)