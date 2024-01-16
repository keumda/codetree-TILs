b, a = list(map(int, input().split()))
if b%2==1:
    b = b - 1

while(a <= b):
    print(b, end=' ')
    b = b - 2