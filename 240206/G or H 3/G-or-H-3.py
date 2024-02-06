n, k = tuple(map(int, input().split()))
commands = [
    tuple(input().split())
    for row in range(n)
]
arr_l = max(commands, key=lambda item: int(item[0]))
arr = [0]*(10000)

for c in commands:
    # print(c)
    idx = int(c[0])
    arr[idx] = c[1]
max_score = 0
for i in range(1, len(arr)-k):
    score = 0
    for j in range(i, i+k+1):
        if arr[j] == 'G':
            score += 1
        if arr[j] == 'H':
            score += 2
    max_score = max(score, max_score)
print(max_score)