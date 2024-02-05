p = input()
cnt = 0
for i in range(len(p)-1):
    if p[i:i+2] == '((':
        for j in range(i+2, len(p)-1):
            if p[j:j+2] == '))':
                cnt += 1
print(cnt)