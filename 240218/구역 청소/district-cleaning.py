x1, x2 = tuple(map(int, input().split()))
x3, x4 = tuple(map(int, input().split()))

if x2 < x3 or x4 < x1:
    area = (x2 - x1) + (x4 - x3)
else:
    area = max(x4, x2) - min(x1, x3)
print(area)