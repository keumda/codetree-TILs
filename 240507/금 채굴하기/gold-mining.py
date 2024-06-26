# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# 주어진 k에 대하여 마름모의 넓이를 반환합니다.
def get_area(k):
    return k * k + (k + 1) * (k + 1)


# 주어진 좌표가 격자에 표함되는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
def get_num_of_gold(row, col, k):
    num_of_gold = 0
    # 방향에 따라 바뀌는 x와 y의 변화량을 정의합니다.
    dxs, dys = [1, 1, -1, -1], [-1, 1, 1, -1]
    
    num_of_gold += grid[row][col] # k = 0 일 때 처리
    
    for curr_k in range(1, k + 1):
        curr_x, curr_y = row - curr_k, col # 순회 시작점 설정
        for dx, dy in zip(dxs, dys):
            for step in range(curr_k):
                if in_range(curr_x, curr_y):
                    num_of_gold += grid[curr_x][curr_y]
                
                curr_x = curr_x + dx
                curr_y = curr_y + dy
    
    return num_of_gold


max_gold = 0

total_gold = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            total_gold += 1
max_k = 0
max_digging_price = total_gold * m
while True:
    max_k += 1
    if get_area(max_k) >= max_digging_price:
        break



# print(max_digging_price, get_area(max_k), max_k)
# 격자의 각 위치가 마름모의 중앙일 때 채굴 가능한 금의 개수를 구합니다.
for row in range(n):
    for col in range(n):
        for k in range(max_k):            
            num_of_gold = get_num_of_gold(row, col, k)
            # print(num_of_gold)
            max_gold = max(max_gold, num_of_gold)
print(max_gold)