n = int(input())
arr = list(map(int, input().split()))

max_m = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                m = arr[i] * arr[j] * arr[k]
                max_m = max(max_m, m)
print(max_m)