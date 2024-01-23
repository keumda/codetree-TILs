n = int(input())
arr = list(map(int, input().split()))

def make_abs(a):
    for i, elem in enumerate(a):
        a[i] = abs(elem)
    return a

make_abs(arr) 
for i in arr:
    print(i, end=' ')