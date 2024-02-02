n = int(input())

arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

def in_range(col, row):
    return col >= 0 and col < n and row >= 0 and row < n

dis, djs = [1, 0, -1, 0], [0, 1, 0, -1]

more_than_three_cnt = 0
for i, row in enumerate(arr):
    for j, col in enumerate(row):
        cnt = 0
        for di, dj in zip(dis, djs):
            check_i, check_j = i + di, j + dj
            # print(check_i, check_j)
            if in_range(check_i, check_j) and arr[check_i][check_j]==1:
                cnt += 1
        if cnt >= 3:
            more_than_three_cnt += 1
print(more_than_three_cnt)