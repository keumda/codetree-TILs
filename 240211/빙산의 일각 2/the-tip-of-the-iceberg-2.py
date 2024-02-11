n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

max_cnt = 0
for i in range(1, 1000):
    cnt = 0
    is_one = False
    for h in arr:
        if h > i:
            if not is_one:
                cnt += 1
                is_one = True
            else:
                is_one = True
        else:
            is_one = False
    # print(i, cnt)
    max_cnt = max(cnt, max_cnt)
print(max_cnt)