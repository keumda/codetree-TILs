n = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

idx = 0
for i in range(n):
    for j in range(n):
        if j >= i:
            print(alpha[idx], end=' ')
            idx = idx + 1
            if idx == len(alpha):
                idx = 0
        else:
            print(' ', end=' ')           
    print()