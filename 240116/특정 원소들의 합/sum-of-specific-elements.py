n = 4
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

s = 0
for idx, i in enumerate(arr):
    s = s + sum(i[:idx+1])
print(s)