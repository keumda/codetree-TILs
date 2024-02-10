n, b = tuple(map(int, input().split()))
arr = []

for i in range(n):
    s = [i+1]
    s= s + list(map(int, input().split()))
    arr.append(s)
# print(arr)
# arr.sort(key = lambda x:x[1]+x[2])
# print(arr)

max_cnt = 0
for i in range(n):
    cnt = 0
    price = 0
    for j in range(n):
        if i != j:
            price += arr[j][1] + arr[j][2]
        else:
            price += arr[i][1]//2 + arr[i][2]
        if price <= b:
            # print(i, j, price, arr[j])
            cnt = arr[j][0]
    max_cnt = max(cnt, max_cnt)
print(max_cnt)