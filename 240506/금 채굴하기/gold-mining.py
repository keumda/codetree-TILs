n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def digging_price(k):
    return (k * k) + (k + 1) * (k + 1)

total_gold = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            total_gold += 1

max_k = 0
max_digging_price = total_gold * m
while True:
    if digging_price(max_k) >= max_digging_price:
        break
    max_k += 1
answer = []
shapes = []

def find_profit(i, j, k):
    if k == max_k:
        return
    # count gold in range and calculate profit for that position
    gold_cnt = count_gold(i, j, k)
    curr_profit = gold_cnt * m - digging_price(k)
    if curr_profit > 0:
        answer.append(gold_cnt)
    find_profit(i, j, k + 1)

def count_gold(i, j, k):
    # print(i, j, k)
    pts = list()
    cnt = 0
    if grid[i][j] == 1:
        cnt += 1
    pts.append([i, j])

    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

    for curr_k in range(1, k+1):
        curr_x, curr_y = i - curr_k, j # 순회 시작점 설정
        for dx, dy in zip(dxs, dys):
            for step in range(curr_k):
                if in_range(curr_x, curr_y):
                    cnt += grid[curr_x][curr_y]
                curr_x = curr_x + dx
                curr_y = curr_y + dy
    return cnt


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n

max_k = 2
for i in range(n):
    for j in range(n):
        find_profit(i, j, 0)

print(max(answer))