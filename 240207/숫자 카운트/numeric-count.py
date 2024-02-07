n = int(input())
guess = []
for _ in range(n):
    # cnt1 means same digit, same number
    # cnt2 means same number but not in a same digit
    g = tuple(map(int, input().split()))
    guess.append(g)

cnt = 0
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if i != j and j != k and i != k:
                first, second, third = i, j, k
                # print(first, second, third)
                successd = True
                for g in guess:
                    n, cnt1, cnt2 = g
                    g_first, g_second, g_third = int(str(n)[0]), int(str(n)[1]), int(str(n)[2])
                    g_cnt1, g_cnt2 = 0, 0

                    if g_first == first:
                        g_cnt1 += 1
                    if g_second == second:
                        g_cnt1 += 1
                    if g_third == third:
                        g_cnt1 += 1

                    if first == g_second or first == g_third:
                        g_cnt2 += 1
                    if second == g_first or second == g_third:
                        g_cnt2 += 1
                    if third == g_first or third == g_second:
                        g_cnt2 += 1

                    # print(n, g_cnt1, g_cnt2)

                    if cnt1 != g_cnt1 or cnt2 != g_cnt2:
                        successd = False

                if successd:
                    cnt += 1
print(cnt)