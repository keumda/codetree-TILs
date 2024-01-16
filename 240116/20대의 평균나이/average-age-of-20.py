s = 0
n = 0
while(True):
    curr = int(input())
    if curr // 10 != 2:
        # print(curr, s, n)
        print(format(s / n, '.2f'))
        break
    s = s + curr
    n = n + 1