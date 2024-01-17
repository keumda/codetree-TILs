n = int(input())

for i in range(n, 0, -1):
    row = '*'*i

    fmt_str = '{0:<'+str(2*n-i)+'}'
    row_added = fmt_str.format(row) + row

    print(row_added)