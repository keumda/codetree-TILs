n = int(input())

max_len = n + (n-1)

for i in range(1, n+1):
    #print(n, i, n - i)
    star_str = '* '*i
    l_space_num = n - i
    print(l_space_num * ' '+star_str)

# for i in range(n, 0, -1):
#     star_str = '* '*i
#     l_space_num = int((max_len - i) / 2)
#     if i == n:
#         l_space_num = 0
#     print(l_space_num*' '+star_str)