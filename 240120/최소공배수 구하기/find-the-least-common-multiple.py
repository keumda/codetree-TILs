n, m = tuple(map(int, input().split()))

def find_common_divider(n, m):
    arr = []
    min_num = min(n, m)
    s = 1
    for i in range(min_num, 1, -1):
        if n%i == 0 and m%i == 0:
            s = i
            break
    return s


cd = find_common_divider(n, m)
cm = n//cd * m//cd * cd
print(cm)