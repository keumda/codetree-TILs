n, s = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

closest_diff = s
for i in range(n):
    for j in range(i+1, n):
        s_sum = 0
        for k in range(n):
            if k != i and k != j:
                # print(nums[k], end=' ')
                s_sum += nums[k]
        # print(s_sum)
        closest_diff = min(closest_diff, abs(s - s_sum))
print(closest_diff)