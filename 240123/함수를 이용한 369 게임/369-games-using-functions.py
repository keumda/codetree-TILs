a, b = tuple(map(int, input().split()))

def is_3_multi(n):
    return n%3 == 0

def is_3_6_9(n):
    for i in str(n):
        if int(i) == 3 or int(i) == 6 or int(i) == 9:
            return True
    return False

c = 0
for i in range(a, b+1):
    if is_3_6_9(i) or is_3_multi(i):
        c += 1

print(c)