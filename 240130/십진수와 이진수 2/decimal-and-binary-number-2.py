n = input()

def convert_decimal(n):
    converted = 0
    for i in n:
        converted = converted * 2 + int(i)
    return converted

def convert_to_binary(n, d):
    digits = []
    while True:
        if n < d:
            digits.append(n)
            break
        curr = n % d
        digits.append(curr)
        n = n//d
    return ''.join(map(str, digits[::-1]))

print(convert_to_binary(convert_decimal(n)*17, 2))