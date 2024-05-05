n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_val = 0

def get_block_one(i, j):
    global max_val
    array = list()
    for x in range(i, i + 2):
        for y in range(j, j + 2):           
            array.append(grid[x][y])
    total = sum(array)
    for direction in range(4):
        s = total - array[direction]
        max_val = max(max_val, s)

def get_block_two_v(i, j):
    global max_val
    arr = list()
    for x in range(i, i + 3):
        arr.append(grid[x][j])
    s = sum(arr)
    max_val = max(max_val, s)


# block 1
for i in range(n - 2 + 1):
    for j in range(m - 2 + 1):
        get_block_one(i, j)

# block 2 (vertical)
for i in range(n - 3 + 1):
    for j in range(m):
        get_block_two_v(i, j)
# block 2 (horizontal)       
for i in range(n):
    for j in range(m - 3 + 1):
        s = sum(grid[i][j:j+3])
        max_val = max(max_val, s)

print(max_val)