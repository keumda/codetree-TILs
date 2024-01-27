n = int(input())
seq = list(map(int, input().split()))
arr = []
answer = [0]*n
for i, elem in enumerate(seq):
    arr.append((i, elem))
arr.sort(key=lambda x:x[1])

for i, elem in enumerate(arr):
    answer[elem[0]] = i + 1

for idx in answer:
    print(idx, end=' ')