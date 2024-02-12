a, b, c = tuple(map(int, input().split()))

max_a = c // a
max_b = c // b
max_s = 0
for i in range(max_a+1):
    for j in range(max_b+1):
        # print(i, j)
        s = (i*a) + (j*b)
        if s <= c:
            max_s = max(max_s, s)
print(max_s)