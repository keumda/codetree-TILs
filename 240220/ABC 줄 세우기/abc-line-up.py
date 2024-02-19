n = int(input())
arr = list(input().split())
cnt = 0
for i in range(n-1):
    if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        cnt += 1
print(cnt)