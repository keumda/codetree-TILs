n = int(input())

cnt = 1
prev = 0
for _ in range(n):
    curr = int(input())
    # print(prev, curr, cnt)
    if prev != curr:
        prev = curr
    else:
        cnt += 1
print(cnt)