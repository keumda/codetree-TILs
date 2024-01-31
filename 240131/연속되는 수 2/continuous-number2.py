n = int(input())

cnt = 1
max_cnt = 1
prev = 0
for i in range(n):
    curr = int(input())
    # print(prev, curr, cnt)
    if prev != curr or i == n-1:
        prev = curr
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt += 1
    
print(cnt)