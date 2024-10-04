n = int(input())
arr = []

for i in range(n):
    cmdArr = input().split()
    if cmdArr[0] == 'push_front':
        arr = [int(cmdArr[1])]+arr
    if cmdArr[0] == 'push_back':
        arr.append(int(cmdArr[1]))
    if cmdArr[0] == 'pop_front':
        print(arr[0])
        arr = arr[1:]
    if cmdArr[0] == 'pop_back':
        print(arr[-1])
        arr = arr[:-1]
    if cmdArr[0] == 'size':
        print(len(arr))
    if cmdArr[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    if cmdArr[0] == 'front':
        print(arr[0])
    if cmdArr[0] == 'back':
        print(arr[-1])