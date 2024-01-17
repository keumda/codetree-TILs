n = int(input())

# 1   1 2 3 4 (j+1)
# 2   1 2 3


for i in range(n):
    for j in range(n, 0, -1):
        curr = (j) * (i + 1)
        print(curr, end=' ')
    print()