r, c = tuple(map(int, input().split()))

cnt = 1
matrix = [[0 for col in range(c)] for row in range(r)]

while cnt <= (r*c):
    for col in range(c):
        r_idx = 0
        c_idx = col
        while True:
            if (r_idx >= r or c_idx < 0):
                break
            matrix[r_idx][c_idx] = cnt
            cnt += 1
            r_idx += 1
            c_idx -= 1
    for row in range(1, r):
        r_idx = row
        c_idx = c - 1
        while True:
            if (r_idx >= r or c_idx < 0):
                break
            matrix[r_idx][c_idx] = cnt
            cnt += 1
            r_idx += 1
            c_idx -= 1

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=' ')
    print()