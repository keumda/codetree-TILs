import sys

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for row in range(n)
]

def find_dist_squared(x1, y1, x2, y2):
    # print(x1, y1, x2, y2)
    w = (x2 - x1) ** 2
    h = (y2 - y1) ** 2
    return int((w + h))

min_dist_s = sys.maxsize
for i in range(n):
    for j in range(n):
        if i != j:
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            d = find_dist_squared(x1, y1, x2, y2)
            # print(arr[i], arr[j], d)
            min_dist_s = min(min_dist_s, d)
print(min_dist_s)