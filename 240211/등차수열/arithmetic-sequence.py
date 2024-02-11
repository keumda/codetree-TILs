n = int(input())
arr = list(map(int, input().split()))

max_cnt = 0
for k in range(min(arr)+1, max(arr)):
    cnt = 0
    for l in range(1, max(arr)-k+1):
        i, j = k + l, k - l
        # print(i, k, j)
        is_i = False
        is_j = False
        for elem in arr:
            if elem == i:
                is_i = True
            if elem == j:
                is_j = True
        if is_i and is_j:
            cnt += 1
        # print('cnt: ', cnt)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)