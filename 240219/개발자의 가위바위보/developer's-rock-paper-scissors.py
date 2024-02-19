n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 1 r 2 p 3 s
# 1 r 2 s 3 p
# 1 p 2 s 3 r
# 1 p 2 r 3 s
# 1 s 2 r 3 p
# 1 s 2 p 3 r
rpc = ['r', 'p', 's']
max_win = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                s_arr = [rpc[i], rpc[j], rpc[k]]
                # print(i, j, k, s_1, s_2, s_3)
                win_cnt = 0
                for a, b in arr:
                    cur_a, cur_b = s_arr[a-1], s_arr[b-1]
                    if cur_a == 'r' and cur_b == 's':
                        win_cnt += 1
                    if cur_a == 'p' and cur_b == 'r':
                        win_cnt += 1
                    if cur_a == 's' and cur_b == 'p':
                        win_cnt += 1
                max_win = max(max_win, win_cnt)
print(max_win)