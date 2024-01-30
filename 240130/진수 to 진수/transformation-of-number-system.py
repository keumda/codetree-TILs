a, b = tuple(map(int, input().split()))
n = input()

def convert_digit(decimal_num, b):
    digits = []
    while True:
        if decimal_num < b:
            digits.append(decimal_num)
            break
        digits.append(decimal_num%b)
        decimal_num //= b
    converted = ''.join(map(str, digits[::-1]))
    return converted

def convert_decimal(n, a):
    converted = 0
    for i in n:
        converted = converted * a + int(i)
    return converted
        
converted = convert_decimal(n, a)
res = convert_digit(converted, b)
print(res)