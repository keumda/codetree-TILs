n = int(input())

max_len = n + (n-1)

for i in range(1, n+1):
    star_str = '* '*i
    l_space_num = n - i
    print(l_space_num * ' '+star_str)

for i in range(1, n):
    star_str = '* '*(n-i)
    l_space_num = i
    print(l_space_num*' '+star_str)