m, d, m1, d1 = tuple(map(int, input().split()))
target_day = input()

month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_eng = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def total_days(m, d):
    days = d
    for i in range(m):
        days += month_days[i]
    return days

diff = total_days(m1, d1) - total_days(m, d)
target_cnt = diff // 7
if days_eng[diff%7] == target_day:
    target_cnt += 1
print(target_cnt)