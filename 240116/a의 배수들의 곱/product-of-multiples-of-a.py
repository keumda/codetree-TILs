a, b = list(map(int, input().split()))
pd = 1
for i in range(1, b+1):
    if i%a==0:
        pd = pd * i

print(pd)