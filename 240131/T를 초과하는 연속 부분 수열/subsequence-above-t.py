n, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


cnt = 0
max_cnt = 0
for elem in arr:
    curr = elem
    if curr > t:
        cnt += 1
    else:
        cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt
    # print(curr, cnt, max_cnt)

print(max_cnt)