n = int(input())
path = [
    input().split()
    for _ in range(n)
]

final_x, final_y = 0, 0 
for i in path:
    val = int(i[1])
    if i[0]=='E':
        final_x, final_y = final_x + val, final_y
    if i[0]=='W':
        final_x, final_y = final_x - val, final_y
    if i[0]=='S':
        final_x, final_y = final_x, final_y - val
    if i[0]=='N':
        final_x, final_y = final_x, final_y + val
print(final_x, final_y)