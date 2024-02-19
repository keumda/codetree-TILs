a, b, x, y = tuple(map(int, input().split()))

r1 = abs(a - b)
r2 = abs(a - x) + abs(y - b)
r3 = abs(a - y) + abs(x - b)

print(min(r1, r2, r3))