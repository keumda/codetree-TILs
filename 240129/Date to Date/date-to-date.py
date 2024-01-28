m, d, m1, d1 = tuple(map(int, input().split()))

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m_days = d
for i, d in enumerate(month_days):
    if i == m:
        break
    m_days += d

m1_days = d1
for i, d in enumerate(month_days):
    if i == m1:
        break
    m1_days += d

print(m1_days - m_days + 1)