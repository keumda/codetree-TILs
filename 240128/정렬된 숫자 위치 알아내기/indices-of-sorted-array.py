n = int(input())
seq = list(map(int, input().split()))
arr = []
arr2 = []
for i, elem in enumerate(seq):
    arr.append((i+1, elem))
arr.sort(key=lambda x:x[1])

for i, elem in enumerate(arr):
    prev_num, val = elem
    arr2.append((i+1, prev_num, val))
arr2.sort(key=lambda x:x[1])

for elem in arr2:
    print(elem[0], end=' ')