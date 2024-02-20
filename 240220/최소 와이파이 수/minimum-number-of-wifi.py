n, m = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))

cnt = 0
i = 0
while True:
    if i >= n:
        break
    if arr[i] == 1:
        cnt += 1
        i += (2*m) + 1
    else:
        i += 1
print(cnt)