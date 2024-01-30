n, decimal = tuple(map(int, input().split()))

n_digits = []
while True:
    if n < decimal:
        n_digits.append(n)
        break
    curr = n % decimal
    n_digits.append(curr)
    n = n // decimal

for i in n_digits[::-1]:
    print(i, end='')