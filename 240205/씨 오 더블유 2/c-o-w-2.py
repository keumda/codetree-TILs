n = int(input())
p = input()
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if p[i] == 'C' and p[j] == 'O' and p[k] == 'W':
                cnt += 1
print(cnt)