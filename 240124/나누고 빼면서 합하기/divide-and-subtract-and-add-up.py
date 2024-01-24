n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def modify_m_val(m):
    m_cnt = m
    s = 0
    while m_cnt >= 1:
        s += arr[m_cnt-1]
        if m_cnt%2 == 1:
            m_cnt -= 1
        else:
            m_cnt //= 2
    print(s)

modify_m_val(m)