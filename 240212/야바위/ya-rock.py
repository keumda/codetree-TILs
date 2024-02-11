n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_score = 0
for i in range(1, 4):
    score = 0
    stones = [0]*4
    stones[i] = 1
    for (a, b, c) in arr:
        temp = stones[b]
        stones[b] = stones[a]
        stones[a] = temp
        if stones[c] == 1:
            score += 1
    max_score = max(max_score, score)
print(max_score)