n, b = tuple(map(int, input().split()))
prices = [
    int(input())
    for p in range(n)
]

max_cnt = 0
for i in range(n):
    leftover = b
    cnt = 0
    for j in range(n):
        curr = prices[j]
        if i == j:
            curr = prices[j]//2
        leftover = leftover - curr
        if leftover >= 0:
            cnt += 1
        else:
            break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)