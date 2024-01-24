n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for _ in range(m):
    a1, a2 = tuple(map(int, input().split()))
    s = 0
    for i in range(a1-1, a2):
        s += arr[i]
    print(s)