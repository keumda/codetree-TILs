n = int(input())
pts = [
    map(int, input().split())
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
    global lines, n, max_cnt
    if idx == n:
        # print(lines)
        max_cnt = max(max_cnt, len(lines))
        lines = []
        return
    curr_x, curr_y = pts[idx]
    if check_cross(curr_x, curr_y):
        lines.append([curr_x, curr_y])
    backtrack(idx + 1)
    return

backtrack(0)
print(max_cnt)