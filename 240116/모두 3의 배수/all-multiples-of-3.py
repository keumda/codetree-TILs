arr = list(map(int, input().split()))

flag = 1
for i in arr:
    if i%3!=0:
        flag = 0

print(flag)