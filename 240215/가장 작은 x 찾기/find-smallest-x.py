n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
min_x = 10000
for j in range(arr[0][0]//2, arr[0][1]//2+1):
    pass_all = True
    multi_x = j
    for i in range(n):
        multi_x *= 2
        if multi_x < arr[i][0] or multi_x > arr[i][1]:
            pass_all = False
        # print(i+1, j, multi_x, pass_all)
    if pass_all:
        min_x = min(j, min_x)
        # print('yay', min_x)
print(min_x)