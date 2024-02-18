n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

res = 'No'
st = min(arr, key=lambda item: item[0])[0]
end = max(arr, key=lambda item: item[1])[1]
for r_idx in range(len(arr)):
    for i in range(st, end):
        is_all_intersect= True
        for k, (x, y) in enumerate(arr):
            if k != r_idx:
                if i < x or i > y:
                    is_all_intersect = False
                    break
        if is_all_intersect:
            res = 'Yes'
            break
print(res)