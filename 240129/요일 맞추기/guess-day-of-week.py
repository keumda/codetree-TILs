m, d, m1, d1 = tuple(map(int, input().split()))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_eng = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def total_days(m, d):
    days = d
    for i in range(m):
        d += month_days[i]
    return days

diff = total_days(m1, d1) - total_days(m, d)
print(days_eng[diff%7])