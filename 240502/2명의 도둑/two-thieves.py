import sys
sys.setrecursionlimit(200000)

n, m, c = map(int, input().split())
gird = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_weight = 0
res = []

# select m and find max sum
wl = []
pts = []
calc_w = []
max_weight = 0
def find_max_weight(x, y, curr):
    global wl, pts
    if curr == m:
        if sum(wl) <= c:
            weight = sum([x*x for x in wl])
            # print(wl, weight)
            calc_w.append(weight)
        wl = []
        pts = []
        return
    else:
        for i, elem in enumerate(gird[x][y:y+m]):
            if i not in pts:
                wl.append(elem)
                pts.append(i)
                find_max_weight(x, y, curr + 1)        
        return

def select(x, y):
    global calc_w

    find_max_weight(x, y, 0)
    w1 = max(calc_w)
    calc_w = []

    for i in range(n):
        for j in range(n-m+1):
            if x == i and (j >= y and j < y+m):
                continue
            elif x == i and (n - m < m):
                continue
            else:
                find_max_weight(i, j, 0)
                w2 = max(calc_w)
                calc_w = []
                res.append(w1 + w2)
                # print('back:', i, j, w1, w2, w1+w2)
                # print(res)
    return

for x in range(n):
    for y in range(n-m+1):
        # print(x, y)
        select(x, y)

print(max(res))

# 1, 2, 3
# find_max_weight(0, 0, 0)
# print(max(calc_w))
# calc_w = []