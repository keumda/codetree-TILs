a = input()
b = input()

a_list = sorted(a)
b_list = sorted(b)
a = ''.join(a_list)
b = ''.join(b_list)

if a == b:
    print('Yes')
else:
    print('No')