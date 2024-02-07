arr = list(map(int, input().split()))
total = sum(arr)
min_diff = total
for i in range(6):
    for j in range(i+1, 6):
        for k in range(6):
            for l in range(k+1, 6):
                if k != i and k != j and l != i and l != j:
                    team_a = arr[i] + arr[j]
                    team_b = arr[l] + arr[k]
                    team_c = total - team_a - team_b
                    diff = max(team_a, team_b, team_c) - min(team_a, team_b, team_c)
                    min_diff = min(min_diff, diff)
print(min_diff)