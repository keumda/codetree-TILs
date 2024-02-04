r, c = tuple(map(int, input().split()))
arr = []
for _ in range(r):
    row = list(input().split())
    arr.append(row)

first_c = arr[0][0]
if first_c == 'W':
    second_c = 'B'
    third_c = 'W'
else:
    second_c = 'W'
    third_c = 'B'
cnt = 0
for i in range(1, r):
    for j in range(1, c):
        if arr[i][j] == second_c:
            for k in range(i+1, r):
                for l in range(j+1, c):
                    if arr[k][l] == third_c and third_c != arr[r-1][c-1]:
                        cnt += 1
print(cnt)