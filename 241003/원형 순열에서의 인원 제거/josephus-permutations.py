from collections import deque

n, k = map(int, input().split())

q = deque()
for i in range(1, n+1):
    q.append(i)
while len(q) != 0:
    for i in range(k-1):
        front = q.popleft()
        q.append(front)
    print(q.popleft(), end=" ")