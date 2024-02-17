n, k = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]

exploded = {}
for i in range(n):
    for j in range(n):
        if i != j and arr[i] == arr[j]:
            dist = abs(i-j)
            if dist <= k:
                if arr[i] in exploded:
                    exploded[arr[i]] += 1
                else:
                    exploded[arr[i]] = 1
exploded = sorted(exploded.items(), key = lambda item: (item[1], item[0]), reverse = True)
if len(exploded) == 0:
    print(0)
else:
    print(exploded[0][0])