arr = list(map(int, input().split()))
total = sum(arr)
min_diff = total
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            a_sum = arr[i] + arr[j] + arr[k]
            b_sum = total - a_sum
            diff = abs(a_sum - b_sum)
            min_diff = min(min_diff, diff)

print(min_diff)