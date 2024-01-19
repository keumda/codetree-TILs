n, pt_cnt = tuple(map(int, input().split()))
matrix = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(pt_cnt):
    r, c = tuple(map(int, input().split()))
    pt_size = r * c 
    matrix[r-1][c-1] = pt_size

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()