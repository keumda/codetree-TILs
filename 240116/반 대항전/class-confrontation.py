n = int(input())
arr = []
for _ in range(4):
    arr.append(input().split())

max = 0
winner = ''
for i in range(4):
    s = sum(list(map(int, arr[i][1:])))
    crr_class = arr[i][0][:-1]
    print('{0} - {1}'.format(crr_class, s))
    if s > max:
        max = s
        winner = crr_class

print('Class {0} is winner!'.format(winner))