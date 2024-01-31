n, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


cnt = 0
max_cnt = 0
for elem in arr:
    curr = elem
    if curr > t:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0
    # print(curr, cnt, max_cnt)
if max_cnt < cnt:
    max_cnt = cnt
print(max_cnt)