import sys
sys.setrecursionlimit(200000)

n, m, c = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
res = []
wl = list()
max_val = 0
def find_max_weight(curr_idx, curr_w, curr_val):
    global max_val
    if curr_idx == m:
        if curr_w <= c:
            max_val = max(max_val, curr_val)
        return
    find_max_weight(curr_idx + 1, curr_w, curr_val)
    find_max_weight(curr_idx + 1, curr_w+wl[curr_idx], 
                    curr_val+wl[curr_idx]*wl[curr_idx])

def find_max(x, y):
    global wl, max_val, grid
    wl = grid[x][y:y + m]
    max_val = 0
    find_max_weight(0, 0, 0)
    return max_val

def select(x, y):
    w1 = find_max(x, y)

    for i in range(n):
        for j in range(n-m+1):
            if x == i:
                # y:0, j: 1
                if(j > y and j < y + m):
                    continue
                if(j+m > y and j+m < y + m):
                    continue
                if j == y and j + m == y + m:
                    continue
                else:
                    w2 = find_max(i, j)
                    res.append(w1 + w2)
            else:
                w2 = find_max(i, j)
                res.append(w1 + w2)
    return

for x in range(n):
    for y in range(n-m+1):
        select(x, y)

print(max(res))