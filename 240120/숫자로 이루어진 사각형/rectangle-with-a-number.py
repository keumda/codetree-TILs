def print_num_rect(n):
    st = 1
    for i in range(n):
        for j in range(n):
            print(st, end=' ')
            st += 1
            if st > 9:
                st = 1
        print()

n = int(input())
print_num_rect(n)