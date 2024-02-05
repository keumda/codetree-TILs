import sys

n = int(input())
check_pts = []
for _ in range(n):
    pt = tuple(map(int, input().split()))
    check_pts.append(pt)

def find_dist(arr):
    dist = 0
    # print(arr)
    for i in range(len(arr)-1):
        dist += abs(arr[i][0] - arr[i+1][0]) + abs(arr[i][1] - arr[i+1][1])
        # print(abs(arr[i][0] - check_pts[i+1][0]), abs(check_pts[i][1] - check_pts[i+1][1]))
    # print('=============')
    return dist

min_dist = sys.maxsize
for i in range(1, n-1):
    dist = find_dist(check_pts[:i] + check_pts[i+1:])        
    min_dist = min(dist, min_dist)
print(min_dist)