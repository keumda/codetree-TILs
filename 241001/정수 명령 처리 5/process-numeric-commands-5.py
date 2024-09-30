n = int(input())
arr = []
for i in range(n):
    cmdArr = input().split()
    if cmdArr[0] == 'push_back':
        arr.append(cmdArr[1])
    if cmdArr[0] == 'pop_back':
        arr.pop()
    if cmdArr[0] == 'size':
        print(len(arr))
    if cmdArr[0] == 'get':
        idx = int(cmdArr[1])
        print(arr[idx-1])