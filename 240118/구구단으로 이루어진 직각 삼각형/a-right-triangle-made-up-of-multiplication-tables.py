n = int(input())

# 5
# 4
# 3
# 2
# 1

for i in range(n):
    for j in range(1, n-i+1):
        print('{} * {} = {}'.format(i+1, j, (i+1)*j), end='')
        if j != n-i:
            print(' / ', end='')
    print()