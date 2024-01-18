a, b = tuple(map(int, input().split()))

remainder_arr = [0]*10
while a > 1:
    r = a % b
    remainder_arr[r] += 1
    a //= b

s = 0
for i in remainder_arr:
    s += i **2
print(s)