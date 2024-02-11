t, a, b = tuple(map(int, input().split()))
arr = [
    input().split()
    for _ in range(t)
]
# arr.sort(key = lambda x:x[1])
# print(arr)

def is_special(n):
    ds1, dn2 = 1000, 1000
    for (c, x) in arr:
        x = int(x)
        if c == 'S':
            ds = abs(n-x)
            ds1 = min(ds, ds1)
        else:
            dn = abs(n-x)
            dn2 = min(dn, dn2)
    if ds1 <= dn2:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if is_special(i):
        cnt += 1
print(cnt)