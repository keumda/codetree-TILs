n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_l = 100
for i in range(n):
    min_x = 100
    max_x = 0
    for j in range(n):
        if j != i:
            min_x = min(min_x, arr[j][0])
            max_x = max(max_x, arr[j][1])
    l = max_x - min_x
    min_l = min(min_l, l)
print(min_l)