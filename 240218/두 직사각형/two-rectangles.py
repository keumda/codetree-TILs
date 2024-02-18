x1, y1, x2, y2 = tuple(map(int, input().split()))
x3, y3, x4, y4 = tuple(map(int, input().split()))

if x3 > x2 or x1 > x4 or y1 > y4 or y3 > y2:
    print('nonoverlapping')
else:
    print('overlapping')