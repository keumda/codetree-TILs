n = int(input())
arr = []
for i in range(n):
    cmdArr = input().split()
    if cmdArr[0] == 'push':
        arr.append(cmdArr[1])
    if cmdArr[0] == 'pop':
        last = arr.pop()
        print(last)
    if cmdArr[0] == 'size':
        print(len(arr))
    if cmdArr[0] == 'empty':
        if len(arr) > 0:
            print(0)
        else:
            print(1)
    if cmdArr[0] == 'top':
        print(arr[-1])