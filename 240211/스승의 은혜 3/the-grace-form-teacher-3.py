n, b = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for r in range(n)
]
arr.sort(key = lambda x:(x[0]+x[1]))
# print(arr)

max_cnt = 0
for i in range(n):
    cnt = 0
    price = 0
    # others = arr[:i]+arr[i+1:]
    # print(others)
    for j, (p, s) in enumerate(arr):
        if j == i:
            price += (p//2 + s)
        else:
            price += (p + s)
        if price <= b:
            cnt += 1
    max_cnt = max(max_cnt, cnt)


    # for j in range(n):
    #     if i != j:
    #         price += arr[j][1] + arr[j][2]
    #     else:
    #         price += arr[i][1]//2 + arr[i][2]
    #     if price <= b:
    #         # print(i, j, price, arr[j])
    #         cnt += 1
    # max_cnt = max(cnt, max_cnt)
print(max_cnt)