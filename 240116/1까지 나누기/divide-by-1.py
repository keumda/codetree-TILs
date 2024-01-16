n = int(input())
val = n

for i in range(1, n+1):
    val = val / i
    if val <= 1:
        print(i)
        break