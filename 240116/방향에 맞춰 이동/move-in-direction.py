n = int(input())
path = [
    input().split()
    for _ in range(n)
]

cur_x = 0
cur_y = 0
#print(path)

for i in path:
    val = int(i[1])
    if i[0]=='N':
        cur_y = cur_y+val
    if i[0]=='S':
        cur_y = cur_y-val
    if i[0]=='E':
        cur_x = cur_x+val
    if i[0]=='W':
        cur_x = cur_x+val
print(cur_x, cur_y)