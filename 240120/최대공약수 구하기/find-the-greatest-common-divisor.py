def max_divider(n, m):
    min_num = min(n, m)
    for i in range(min_num, 0, -1):
        if n%i == 0 and m%i == 0:
            print(i)
            break

a, b = tuple(map(int, input().split()))
max_divider(a, b)