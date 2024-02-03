n = int(input())

mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3,
}
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
total_t = 0
i, j = 0, 0
res = -1

def move(d, t):
    global i, j, res, total_t
    for sec in range(t):
        i, j = i + di[mapper[d]], j + dj[mapper[d]]
        total_t += 1
        if i == 0 and j == 0:
            res = total_t
            return True
    return False


for _ in range(n):
    d, t = tuple(input().split())
    t = int(t)
    done = move(d, t)
    if done:
        break
    
print(res)