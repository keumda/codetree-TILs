n = int(input())
arr = list(map(int, input().split()))
max_sum = -1
for i in range(n):
    for j in range(i+2, n):
        s = arr[i] + arr[j]
        max_sum = max(s, max_sum)
print(max_sum)