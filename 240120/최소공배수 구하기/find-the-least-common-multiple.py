n, m = tuple(map(int, input().split()))

def find_common_divider(n, m):
    arr = []
    min_num = min(n, m)
    for i in range(2, min_num+1):
        if n%i == 0 and m%i == 0:
            arr.append(i)
    return arr

s = 1
for elem in find_common_divider(n, m):
    s *= elem
print(s)