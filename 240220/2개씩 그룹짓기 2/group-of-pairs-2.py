n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr1 = arr[:n]
arr2 = arr[n:]
# print(arr1, arr2)
min_diff = 1000000001
for i in range(n):
    diff = arr2[i] - arr1[i]
    min_diff = min(min_diff, diff)
print(min_diff)