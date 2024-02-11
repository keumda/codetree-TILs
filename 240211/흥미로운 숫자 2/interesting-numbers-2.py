x, y = tuple(map(int, input().split()))

def is_interesting(n):
    d = {}
    n = str(n)
    for a in n:
        if d.get(a):
            d[a] = d[a] + 1
        else:
            d[a] = 1
    if len(d) == 2 and (d[n[0]] == 1 or d[n[0]] == len(n)-1):
        return True
    else:
        return False

cnt = 0
for i in range(x, y+1):
    if is_interesting(i):
        cnt += 1
print(cnt)