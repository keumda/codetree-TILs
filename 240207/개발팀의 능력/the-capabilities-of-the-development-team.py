import sys

arr = list(map(int, input().split()))
total = sum(arr)
is_possible = False
min_diff = sys.maxsize

for i in range(5):
    team_c = arr[i]
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            team_b = arr[j] + arr[k]
            team_a = total - team_c - team_b
            if team_a != team_b and team_b != team_c and team_c != team_a:
                # print(team_a, team_b, team_c)
                is_possible = True
                diff = max(team_a, team_b, team_c) - min(team_a, team_b, team_c)
                min_diff = min(min_diff, diff)

if is_possible:
    print(min_diff)
else:
    print(-1)