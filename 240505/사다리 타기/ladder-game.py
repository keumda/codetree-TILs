n, m = map(int, input().split())
status = [
    list(map(int, input().split()))
    for _ in range(m)
]
curr_status = list()
min_len = m

def calc(grid):
    res = [0, 0, 0, 0]
    grid = sorted(grid, key=lambda x: x[1])
    
    for i in range(1, n + 1):
        position = i
        b = 0
        a = i
        while True:
            if find_next(a, b, grid):
                if next_pair[0] == a:
                    a += 1
                else:
                    a -= 1
                b = next_pair[1]
            else:
                res[a - 1] = position
                break
    return ''.join(str(x) for x in res)

next_pair = list()    
def find_next(a, b, grid):
    global next_pair
    next_pair = list()
    is_exist = False

    for x, y in grid:
        if (x == a or x == a - 1) and y > b:
            next_pair = [x, y]
            is_exist = True
            break
    return is_exist

res = calc(status)
def choose(idx, cnt):
    global curr_status, min_len
    curr_res = calc(curr_status)
    # if idx == 1:
    #     print(curr_status, curr_res)
    
    if res == curr_res:
        # print(res, curr_res, len(curr_status))
        # print(curr_status)
        min_len = min(min_len, len(curr_status))
        curr_status = []
        return
    if cnt == m or idx == m:
        curr_status = []
        return
    if status[idx] not in curr_status:
        curr_status.append(status[idx])
    for i in range(idx + 1, m):
        if i not in curr_status:
            curr_a, curr_b = status[i]
            curr_status.append([curr_a, curr_b])
            choose(idx + 1, cnt + 1)

for idx in range(m):
    choose(idx, 1)
print(min_len)