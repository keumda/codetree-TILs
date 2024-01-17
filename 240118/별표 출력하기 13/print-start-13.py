from collections import deque

n = int(input())
l = []

for i in range(1, n+1):
    l.append(i)
res = deque(l)
res2 = []

cnt = 1
while cnt != n+1:
    if cnt%2==1:
        v = res.pop()
    else:
        v = res.popleft()
    star_str = '* '*v
    res2.append(star_str)
    print(star_str)

    cnt=cnt+1

for i in range(len(res2)-1, -1, -1):
    print(res2[i])