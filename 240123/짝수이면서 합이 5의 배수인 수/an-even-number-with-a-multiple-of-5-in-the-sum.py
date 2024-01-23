n = int(input())

def validate_5(n):
    digit_s = 0
    for i in str(n):
        digit_s += int(i)
    if n%2 == 0 and digit_s%5 == 0:
        print('Yes')
    else:
        print('No')

validate_5(n)