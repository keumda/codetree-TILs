n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

res = 'No'
st = min(arr, key=lambda item: item[0])[0]
end = max(arr, key=lambda item: item[1])[1]
for i in range(st, end):
    is_all_intersect= True
    for x, y in arr:
        if i < x or i > y:
            is_all_intersect = False
            break
    if is_all_intersect:
        res = 'Yes'
        break
print(res)