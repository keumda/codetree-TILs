n = int(input())
pts = [
    tuple(map(int, input().split()))
    for t in range(n)
]

def r_triangle(pt1, pt2, pt3):
    x1, y1 = pt1
    x2, y2 = pt2
    x3, y3 = pt3

    if (x1 == x2 or x2 == x3 or x1 == x3) and (y1 == y2 or y2 == y3 or y1 == y3):
        return True
    else:
        return False

max_area_d = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            pt1, pt2, pt3 = pts[i], pts[j], pts[k]
            # print(r_triangle(pt1, pt2, pt3))
            if r_triangle(pt1, pt2, pt3):
                x1, y1 = pt1
                x2, y2 = pt2
                x3, y3 = pt3
                area_d = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
                max_area_d = max(max_area_d, area_d)
print(max_area_d)