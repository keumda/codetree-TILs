n = int(input())
st = input()

max_min_cnt = 0
for i in range(n):
    s = st
    if st[i] == '0':
        s = st[:i]+'1'+st[i+1:]
    min_cnt = 21
    cnt = 21
    for j in range(n):
        if s[j]=='1':
            min_cnt = min(min_cnt, cnt)
            cnt = 0
        else:
            cnt += 1
        # print(cnt, min_cnt)
    max_min_cnt = max(min_cnt, max_min_cnt)
print(max_min_cnt)