import sys

n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

min_cost = sys.maxsize
for i in range(1, 10001):
    cost = 0
    max_limit = i + k
    for elem in arr:
        if elem < i:
            cost += abs(i - elem)
        elif elem > max_limit:
            cost += abs(elem - max_limit)
        else:
            continue
    min_cost = min(min_cost, cost)
print(min_cost)