n = int(input())
arr = list(map(int, input().split()))

min_diff = 100

# 오름차순으로 주어진다!
for i in range(1, n):
    diff = arr[i] - arr[i-1]
    if diff < min_diff:
        min_diff = diff

print(min_diff)