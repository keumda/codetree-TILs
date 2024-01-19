a = input()
command = input()

total_step_cnt = 0
for c in command:
    if c == 'L':
        total_step_cnt -= 1
    if c == 'R':
        total_step_cnt += 1

if total_step_cnt < 0:
    abs_step_cnt = abs(total_step_cnt)
    a = a[abs_step_cnt:] + a[:abs_step_cnt]
else:
    a = a[:total_step_cnt] + a[total_step_cnt:]

print(a)