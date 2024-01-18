a, b = list(map(int, input().split()))

remainder_arr = [0 for i in range(b)]

while (a > 1):
    r = a % b
    remainder_arr[r] = remainder_arr[r] + 1
    q = a // b
    a = q

s = 0
for i in remainder_arr:
    s = s + (i*i)
print(s)