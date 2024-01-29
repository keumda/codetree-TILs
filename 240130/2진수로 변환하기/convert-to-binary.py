n = int(input())

digits = []
while True:
    if n < 2:
        digits.append(n)
        break
    curr = n % 2 
    digits.append(curr)
    n //= 2

for elem in digits[::-1]:
    print(elem, end='')