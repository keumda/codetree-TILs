b, a = list(map(int, input().split()))

if b%2==0:
    b=b-1

for i in range(b, a-1, -2):
    print(i, end=' ')