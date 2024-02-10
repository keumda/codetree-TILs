x, y = tuple(map(int, input().split()))

max_sum = 0
for i in range(x, y+1):
    digit_sum = 0
    for s in str(i):
        digit_sum += int(s)
    max_sum = max(digit_sum, max_sum)
print(max_sum)