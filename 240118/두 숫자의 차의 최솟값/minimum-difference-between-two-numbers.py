n = int(input())
arr = list(map(int, input().split()))

min_diff = 100

for i in range(n):
    for j in range(i+1, n):
        diff = abs(arr[i] - arr[j])
        if diff < min_diff:
            min_diff = diff

print(min_diff)