n, k, T = list(input().split())
arr = []

for _ in range(int(n)):
    arr.append(input())
arr.sort()

ordinal = 0
for elem in arr:
    if elem[:len(T)] == T:
        ordinal += 1
        if ordinal == int(k):
            print(elem)