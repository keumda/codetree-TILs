r, c = tuple(map(int, input().split()))

matrix = [[0 for col in range(c)] for row in range(r)]

num = 0
for j in range(c):
    if (j + 1) % 2 != 0:
        for i in range(r):
            matrix[i][j] = num
            num += 1
    else:
        for i in range(r-1, -1, -1):
            matrix[i][j] = num
            num += 1

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()