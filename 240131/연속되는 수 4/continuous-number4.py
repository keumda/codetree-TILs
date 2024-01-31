n = int(input())

prev = int(input())
cnt = 1
max_cnt = 1
for _ in range(n-1):
    curr = int(input())
    # print(prev, curr, cnt)
    if prev >= curr:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1
    else:
        cnt += 1
    prev = curr
    

if max_cnt < cnt:
    max_cnt = cnt

print(max_cnt)