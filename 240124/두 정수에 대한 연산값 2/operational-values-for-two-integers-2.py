a, b = tuple(map(int, input().split()))

def change_num(a, b):
    if a < b:
        a = a + 10
        b = 2 * b
    else:
        a = 2 * a
        b = b + 10
    return a, b

a, b = change_num(a, b)
print(a, b)