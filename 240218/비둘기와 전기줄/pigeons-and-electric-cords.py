n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
for num in range(1, 11):
    is_first = True
    cur_side = 0
    for x, side in arr:
        if x == num:
            if is_first:
                is_first = False
                cur_side = side
                # print(num, side)
                # cnt += 1
            if cur_side != side:
                cur_side = side
                # print(num, side)
                cnt+= 1
print(cnt)