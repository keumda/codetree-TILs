n = int(input())
arr = list(map(int, input().split()))

for i, elem in enumerate(arr):
    if (i+1)%2 == 1:
        sub_arr = arr[:i+1]
        sub_arr.sort()
        mid = sub_arr[len(sub_arr)//2]
        print(mid, end=' ')