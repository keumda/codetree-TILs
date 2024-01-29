def calc_min(d, h, m):
    total_min = m
    for i in range(h):
        total_min += 60
    for i in range(d):
        total_min += 24 * 60
    return total_min

a, b, c = tuple(map(int, input().split()))
print(calc_min(a, b, c)-calc_min(11, 11, 11))