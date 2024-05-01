import sys
sys.setrecursionlimit(400000)

n, m, c = map(int, input().split())
gird = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_weight = 0
res = []

def find_weight(x, y):
    res = []
    w = 0
    # print('x, y)
    for i in range(y, y+m):
        w += gird[x][i]
        if w > c:
            break
        res.append(gird[x][i])
    total = sum([x*x for x in res])
    return total

def backtrack(x, y):
    w1 = find_weight(x, y)
    for i in range(n):
        for j in range(n-m+1):
            if i != x or j != y: 
                if x == i:
                    if (i >= y and i <= y + m) or (i + m >= y and i + m <= y + m):
                        break
                    else:
                        w2 = find_weight(i, j)
                        res.append(w1 + w2)
                        # print('back:', i, j, w1, w2, w1+w2)
                else:
                    w2 = find_weight(i, j)
                    res.append(w1 + w2)
                    # print('back:', i, j, w1, w2, w1+w2)
            # backtrack(x+1, y+1)     
    return

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for x in range(n):
    for y in range(n-m+1):
        # print('call', x, y)
        backtrack(x, y)

print(max(res))