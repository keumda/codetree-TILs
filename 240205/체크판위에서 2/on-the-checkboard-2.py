r, c = tuple(map(int, input().split()))
arr = []
for _ in range(r):
    row = list(input().split())
    arr.append(row)

curr_c = arr[0][0]
cnt = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        if curr_c != arr[i][j]:
            curr_c = arr[i][j]
            for k in range(i+1, r-1):
                for l in range(j+1, c-1):
                    if curr_c != arr[k][l]:
                        cnt += 1     
print(cnt)