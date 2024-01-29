m, d, m1, d1 = tuple(map(int, input().split()))
target_day = input()

month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_eng = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def total_days(m, d):
    days = d
    for i in range(m):
        days += month_days[i]
    return days

target_cnt = 0
diff = total_days(m1, d1) - total_days(m, d)
target_cnt += diff // 7

if diff < 7 and target_day == 'Mon':
    target_cnt += 1
if days_eng[diff%7] == target_day:
    target_cnt += 1
print(target_cnt)