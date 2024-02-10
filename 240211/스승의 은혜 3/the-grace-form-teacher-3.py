n, b = tuple(map(int, input().split()))
arr = []

for i in range(n):
    s = [i+1]
    s= s + list(map(int, input().split()))
    arr.append(s)
arr.sort(key = lambda x:x[1]+x[2])

max_cnt = 0
for i in range(n):
    price = arr[i][1]//2 + arr[i][2]
    cnt = 0
    for j in range(n):
        if i != j:
            if price > b:
                # print(i, j)
                cnt = arr[j-1][0]
                break
            price += arr[j][1] + arr[j][2]
    max_cnt = max(cnt, max_cnt)
print(max_cnt)