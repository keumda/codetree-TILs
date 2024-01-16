a, b = list(map(int, input().split()))

if a % 2 == 1:
    a = a + 1

while (a <= b):
    print(a, end=' ')
    a = a + 2