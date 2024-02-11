x, y = tuple(map(int, input().split()))

def is_p(n):
    n = str(n)
    if len(n)%2 == 0:
        a = n[:len(n)//2]
    else:
        a = n[:len(n)//2+1]
    b = n[len(n)//2:]
    b = b[::-1]

    # print(a, b)
    if a == b:
        return True
    else:
        return False

cnt = 0
for i in range(x, y+1):
    if is_p(i):
        cnt += 1
print(cnt)