n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
max_s = 0
for i in range(n-k+1):
    s = sum(arr[i:i+k])
    # print(arr[i:i+k], s)
    max_s = max(max_s, s)

print(max_s)