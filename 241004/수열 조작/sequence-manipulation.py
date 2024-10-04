n = int(input())

arr = []
for i in range(1, n+1):
    arr.append(i)

while True:
    if len(arr) == 1:
        break
    arr = arr[1:]
    first = arr[0]
    arr = arr[1:] + [first]
print(arr[0])