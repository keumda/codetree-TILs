k, n = tuple(map(int, input().split()))
rankings = [
    tuple(map(int, input().split()))
    for r in range(k)
]
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            a, b = i, j
            is_a_winner = True
            for game in rankings:
                for k, r in enumerate(game):
                    # print(i, j, k, r)
                    if r == a:
                        a_r = k
                    if r == b:
                        b_r = k    
                if a_r > b_r:
                    is_a_winner = False
            if is_a_winner:
                cnt += 1
print(cnt)