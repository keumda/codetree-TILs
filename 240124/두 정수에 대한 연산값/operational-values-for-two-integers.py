a, b = tuple(map(int, input().split()))

def change_num(a, b):
    if a > b:
        a = a + 25
        b = 2 * b
    else:
        b = b + 25
        a = 2 * a
    return a, b

a, b = change_num(a, b)
print(a, b)