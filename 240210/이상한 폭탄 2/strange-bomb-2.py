n, k = tuple(map(int, input().split()))
bombs = [
    int(input())
    for r in range(n)
]
max_bomb = -1
for i in range(n):
    for j in range(i+1, n):
        # print(bombs[i], bombs[j], abs(bombs[i]-bombs[j]))
        if bombs[i] == bombs[j] and abs(bombs[i]-bombs[j]) <= k:
            max_bomb = max(bombs[i], bombs[j], max_bomb)
print(max_bomb)