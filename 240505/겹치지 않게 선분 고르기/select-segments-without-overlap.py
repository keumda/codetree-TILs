n = int(input())
pts = [
    list(map(int, input().split()))
    for _ in range(n)
]
lines = []
max_cnt = 0

def check_cross(x, y):
    for line in lines:
        i, j = line
        if (x >= i and x <= j) or (y <= j and y <= j):
            # print(x, y, i, j, 'why')
            return False
    return True

def backtrack(idx):
    global lines, n, max_cnt, pts
    if idx == n:
        max_cnt = max(max_cnt, len(lines))
        lines = []
        return
    # print(pts[idx])
    for i in range(idx, n):
        if i != idx:
            curr_x, curr_y = pts[i]
            if check_cross(curr_x, curr_y):
                lines.append([curr_x, curr_y])
    backtrack(idx + 1)
    return

for i in range(n):
    curr_x, curr_y = pts[i]
    if check_cross(curr_x, curr_y):
        lines.append([curr_x, curr_y])
    backtrack(i)

print(max_cnt)