n = int(input())

for i in range(n):
    for j in range(n, 0, -1):
        curr = j * (i + 1)
        print(curr, end=' ')
    print()