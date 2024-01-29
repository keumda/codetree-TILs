m, d, m1, d1 = tuple(map(int, input().split()))
target_day = input()

month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_eng = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
target_day_idx = 0
for i, elem in enumerate(days_eng):
    if target_day == elem:
        target_day_idx = i


def total_days(m, d):
    days = d
    for i in range(m):
        days += month_days[i]
    return days

target_cnt = 0
diff = total_days(m1, d1) - total_days(m, d)
target_cnt = diff // 7

# print(diff, target_cnt, diff%7, target_day_idx)

if diff%7 >= target_day_idx:
    target_cnt += 1
print(target_cnt)