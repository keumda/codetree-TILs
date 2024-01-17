n = int(input())

for i in range(n):
    st = n - i
    while st <= n:
        print(st, end=' ')
        st = st + 1
    print()