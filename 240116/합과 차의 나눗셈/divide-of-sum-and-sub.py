arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

plus = a + b
minus = a - b

print(round(plus / minus, 2))