n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def is_possible(max_val):
    available_idx = []
    for idx, elem in enumerate(arr):
        if elem <= max_val:
            available_idx.append(idx)
    if len(available_idx) <= 1:
        return False
    # print(max_val, available_idx)
    for j in range(1, len(available_idx)):
        dist = available_idx[j] - available_idx[j-1]
        if dist > k:
            return False
    return True



minmax = 10000
for i in range(max(arr)+1):
    if is_possible(i):
        minmax = min(minmax, i)
print(minmax)