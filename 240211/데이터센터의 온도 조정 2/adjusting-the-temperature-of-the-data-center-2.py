n, c, g, h = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
max_prod = 0
# test case: x < ta, ta < x < tb, tb < x
# lowest ta, highest tb 

min_ta = 1000
max_tb = 0
for (ta, tb) in arr:
    min_ta = min(ta, min_ta)
    max_tb = max(tb, max_tb)
# print(min_ta, max_tb)
for i in range(min_ta-1, max_tb+2):
    total_prod = 0
    for (ta, tb) in arr:
        if ta > i:
            total_prod += c
        elif i >= ta and i <= tb:
            total_prod += g
        else:
            total_prod += h
    max_prod = max(max_prod, total_prod)
print(max_prod)