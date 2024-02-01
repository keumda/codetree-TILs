n, m, k = tuple(map(int, input().split()))
students = [0]*n
res = -1
for _ in range(m):
    s = int(input())
    students[s-1] += 1
    if students[s-1] >= k:
        res = s
        break
print(res)