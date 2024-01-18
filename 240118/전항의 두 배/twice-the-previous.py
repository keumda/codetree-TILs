first, second = list(map(int, input().split()))
n = 10

print(first, second, end=' ')
for i in range(n - 2):
    curr = (first*2) + second
    print(curr, end=' ')
    first = second
    second = curr