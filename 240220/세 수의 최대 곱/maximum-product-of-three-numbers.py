n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
# all positives
m1 = arr[-1] * arr[-2] * arr[-3]
# one positive, two negatives
m2 = arr[-1] * arr[0] * arr[1]

print(max(m1, m2))