n = int(input())

heights = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if heights[i] < heights[j] and heights[j] < heights[k]:
                cnt += 1

print(cnt)