n = int(input())

matrix = [
    [0 for _ in range(n)]
    for _ in range(n)
]

is_going_up = True
num = 1
for col_idx in range(n-1, -1, -1):
    if is_going_up:
        for row_idx in range(n-1, -1, -1):
            matrix[row_idx][col_idx] = num
            num += 1
        is_going_up = False
    else:
        for row_idx in range(n):
            matrix[row_idx][col_idx] = num
            num += 1
        is_going_up = True

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()