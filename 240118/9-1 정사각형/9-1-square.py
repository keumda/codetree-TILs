n = int(input())

x = 9
cnt = x
for i in range(n):
    for j in range(n):
        if cnt == 0:
            cnt = x
        print(cnt, end='')
        cnt = cnt - 1
    print()