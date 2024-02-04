p = input()

cnt = 0
idx = 0
for i in range(len(p)):
    for j in range(i+1, len(p)):
        # print(p[i], p[j])
        if p[i] == '(' and p[j] == ')':
            cnt += 1
print(cnt)