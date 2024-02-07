n = int(input())
a,b,c = tuple(map(int, input().split()))
x,y,z = tuple(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if (abs(a - i) <= 2 or abs(a - i) >= n - 2) \
                and (abs(b - j) <= 2 or abs(b - j) >= n - 2) \
                and (abs(c - k) <= 2 or abs(c - k) >= n - 2):
                # print(i, j, k)
                cnt += 1
            elif (abs(x - i) <= 2 or abs(x - i) >= n - 2) \
                and (abs(y - j) <= 2 or abs(y - j) >= n - 2)\
                and (abs(z - k) <= 2 or abs(z - k) >= n - 2):
                # print(i, j, k)
                cnt += 1
               
print(cnt)