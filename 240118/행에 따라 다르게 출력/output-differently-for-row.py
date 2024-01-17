n = int(input())

num = 0
for i in range(n):
    for j in range(n):
        if (i+1)%2==1:
            num = num + 1
        else:
            num = num + 2
        print(num, end=' ')
    print()