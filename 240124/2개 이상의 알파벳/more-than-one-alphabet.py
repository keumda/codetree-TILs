a = input()

def is_there_two(a):
    alpha = a[0]
    cnt = 1
    for c in a[1:]:
        if c != alpha:
            return True
    return False

if is_there_two(a):
    print('Yes')
else:
    print('No')