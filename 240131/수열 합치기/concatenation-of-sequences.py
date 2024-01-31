n, m = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a + b
c.sort()
for elem in c:
    print(elem, end=' ')