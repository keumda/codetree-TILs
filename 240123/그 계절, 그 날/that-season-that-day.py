y, m, d = tuple(map(int, input().split()))

def is_leap(y):
    if y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

def find_season(m):
    if m >= 3 and m <= 5:
        return 'Spring'
    if m >= 6 and m <= 8:
        return 'Summer'
    if m >= 9 and m <= 11:
        return 'Fall'
    if m == 12 or m <= 2:
        return 'Winter'

def is_valid_date(y, m, d):
    if m > 12 or 1 < 0:
        return False
    if m in [1, 3, 5, 7, 8, 10, 12] and d > 31:
        return False
    if m in [4, 6, 9, 11] and d > 30:
        return False
    if m == 2:
        if is_leap(y) and d > 29:
            return False
        if not is_leap(y) and d > 28:
            return False
    return True

if is_valid_date(y, m, d):
    print(find_season(m))
else:
    print(-1)