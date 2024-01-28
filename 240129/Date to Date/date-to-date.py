m, d, m1, d1 = tuple(map(int, input().split()))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m_days = d
for i in range(m+1):
    m_days += month_days[i]

m1_days = d1
for i in range(m1+1):
    m1_days += month_days[i]

print(m1_days - m_days)