n = int(input())

print('* '*n)
for i in range(1, n):
    star_str = '* '*(i)
    space_num = (2*n)-(2*i)-2
    ending_str = (' '*space_num)+'*'
    print(star_str + ending_str)