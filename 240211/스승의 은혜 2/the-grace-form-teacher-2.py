n, b = tuple(map(int, input().split()))
prices = [
    int(input())
    for p in range(n)
]

max_cnt = 0
for i in range(n):
    price = 0
    cnt = 0
    for j in range(n):
        if i != j:
            price += prices[j]
        else:
            price += prices[j]//2
        if price <= b:
            cnt += 1
        else:
            break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)