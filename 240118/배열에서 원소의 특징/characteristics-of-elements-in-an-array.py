l = list(map(int, input().split()))

for i, elem in enumerate(l):
    if elem % 3 == 0:
        idx = i - 1
        if idx < 0:
            idx = 0
        print(l[idx])
        break