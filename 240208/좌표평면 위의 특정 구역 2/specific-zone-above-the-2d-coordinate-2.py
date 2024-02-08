import sys

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for elem in range(n)
]

def rect_area(w, h):
    return w * h

min_a = sys.maxsize
for i in range(n):
    min_x, min_y = 40001, 40001
    max_x, max_y = 0, 0
    for j in range(n):
        if j != i:
            x, y = arr[j]
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x), max(max_y, y)
    a = rect_area(max_x-min_x, max_y-min_y)
    min_a = min(a, min_a)
print(min_a)