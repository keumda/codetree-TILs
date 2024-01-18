n, m = tuple(map(int, input().split()))

matrix1 = []
matrix2 = []
for i in range(n):
    matrix1.append(list(map(int, input().split())))
for i in range(n):
    matrix2.append(list(map(int, input().split())))

res = []
for i in range(n):
    row = [0]*m
    for j in range(m):
        if matrix1[i][j] != matrix2[i][j]:
            row[j] = 1
        print(row[j], end=' ')
    res.append(row)
    print()