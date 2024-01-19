a = input()
command = input()

total_step_cnt = 0
for c in command:
    if c == 'L':
        a = a = a[1:] + a[:1]
    if c == 'R':
        a = a = a[-1:] + a[:-1]
print(a)