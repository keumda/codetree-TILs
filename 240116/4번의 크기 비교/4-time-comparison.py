a = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if a > i:
        print(1)
    else:
        print(0)