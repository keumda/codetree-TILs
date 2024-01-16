arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

plus = a + b
minus = a - b

#format(aa, ".2f")
print(format(plus / minus, ".2f"))