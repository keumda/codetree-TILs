a, b = tuple(map(int, input().split()))

def calc(a, b):
    s = 1
    for _ in range(b):
        s = s * a
    return s

print(calc(a, b))