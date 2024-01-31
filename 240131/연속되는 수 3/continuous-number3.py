n = int(input())

cnt = 1
max_cnt = 0
prev = int(input())
for i in range(n-1):
    curr = int(input())
    # print(prev, curr)
    if prev < 0 and curr < 0:
        cnt += 1
    if prev > 0 and curr > 0:
        cnt += 1
    if (prev > 0 and curr < 0) or (prev < 0 and curr > 0) or i == n-2:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1
    prev = curr

print(max_cnt)