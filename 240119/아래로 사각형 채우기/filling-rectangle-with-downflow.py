n = int(input())

matrix = [[0 for col in range(n)] for row in range(n)]

number = 1
for i in range(n):
    for j in range(n):
        matrix[j][i] = number
        number += 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()