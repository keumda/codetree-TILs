n, b = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
max_cnt = 0
for i in range(n):
    price = arr[i][0]//2 + arr[i][1]
    for j in range(n):
        if i != j:
            if price >= b:
                # print(i, j)
                cnt = j
                break
            price += arr[j][0] + arr[j][1]
    max_cnt = max(cnt, max_cnt)
print(max_cnt)