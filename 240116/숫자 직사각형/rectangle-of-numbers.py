arr = input().split()
r = int(arr[0])
c = int(arr[1])

for i in range(r):
    for j in range(c):
        curr = (j+1)+(i*c)
        print(curr, end=' ')
    print()