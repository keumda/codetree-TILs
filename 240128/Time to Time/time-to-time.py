a, b, c, d = tuple(map(int, input().split()))

a_min = a*60 + b
c_min = c*60 + d

print(c_min - a_min)