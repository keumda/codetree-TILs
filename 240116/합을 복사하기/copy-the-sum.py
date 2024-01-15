from copy import copy

a, b, c = 1, 2, 3
s = a+b+c

a, b, c = copy(s), copy(s), copy(s)
print(a, b, c)