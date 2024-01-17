a, b = list(map(int, input().split()))

row_num = 4
for i in range(1, row_num+1):
    row_val = i*2
    for j in range(b, a-1, -1):
        if j == a:
            print('{} * {} = {}'.format(j, row_val, j*row_val), end='')
        else:
            print('{} * {} = {}'.format(j, row_val, j*row_val), end=' / ')
    print()