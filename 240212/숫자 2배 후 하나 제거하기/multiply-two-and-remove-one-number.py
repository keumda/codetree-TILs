# remaining_arr = [elem for k, elem in enumerate(arr) if k != j]
import sys

n = int(input())
arr = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(n):
    arr_c = arr.copy()
    arr_c[i] = arr_c[i] * 2
    for j in range(n):
        remaining_arr = []
        for k in range(n):
            if k != j:
                remaining_arr.append(arr_c[k])
        # print(remaining_arr)
        sum_diff = 0
        for k in range(len(remaining_arr)-1):
            diff = abs(remaining_arr[k] - remaining_arr[k+1])
            sum_diff += diff
        # print(sum_diff)
        min_sum = min(sum_diff, min_sum)
print(min_sum)