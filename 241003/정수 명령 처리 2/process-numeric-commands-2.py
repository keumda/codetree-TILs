from collections import deque

n = int(input())
arr = deque()
for i in range(n):
    cmdArr = input().split()
    if cmdArr[0] == 'push':
        arr.append(cmdArr[1])
    if cmdArr[0] == 'pop':
        v = arr.popleft()
        print(v)
    if cmdArr[0] == 'size':
        print(len(arr))
    if cmdArr[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    if cmdArr[0] == 'front':
        print(arr[0])