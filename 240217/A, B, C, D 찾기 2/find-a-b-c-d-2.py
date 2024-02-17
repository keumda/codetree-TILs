arr = list(map(int, input().split()))
arr.sort()

for a in range(1, 41):
    for b in range(1, 41):
        for c in range(1, 41):
            for d in range(1, 41):
                if d >= c and c >= b and b >= a:
                    arr2 = [a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]
                    arr2.sort()
                    if arr2 == arr:
                        print(a, b, c, d)