n = int(input())

cnt = 1
max_cnt = 1
prev = int(input())
for i in range(n-1):
    curr = int(input())
    if prev != curr:
        prev = curr
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1
    else:
        cnt += 1
    # print(prev, curr, cnt)

if max_cnt < cnt:
    max_cnt = cnt
print(max_cnt)