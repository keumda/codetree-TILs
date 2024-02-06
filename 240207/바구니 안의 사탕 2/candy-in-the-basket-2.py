n, k = tuple(map(int, input().split()))
arr = [0]*100
for _ in range(n):
    c, idx = tuple(map(int, input().split()))
    arr[idx-1] = arr[idx-1] + c
max_candy_num = 0
for i in range(100-(2*k+1)+1):
    candy_num = sum(arr[i:i+(2*k)+1])
    # print(i, arr[i:i+(2*k)])
    max_candy_num = max(max_candy_num, candy_num)
print(max_candy_num)