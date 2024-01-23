a, b, c = tuple(map(int, input().split()))

def find_min(a, b, c):
    m = min(min(a, b), c)
    return m

print(find_min(a, b, c))