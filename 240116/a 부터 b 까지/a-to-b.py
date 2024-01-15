arr = input().split()
a = int(arr[0])
b = int(arr[1])

c = a
while(c<=b):
    print(c, end=' ')
    if c%2==0:
        c = c+3
    else:
        c = c*2