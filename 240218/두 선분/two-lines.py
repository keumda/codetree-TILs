x, y, x1, y1 = tuple(map(int, input().split()))

if y < x1 or y1 < x1:
    print('nonintersecting')
else:
    print('intersecting')