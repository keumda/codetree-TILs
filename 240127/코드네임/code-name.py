arr = []
for _ in range(5):
    codename, score = tuple(input().split())
    a = (codename, int(score))
    arr.append(a)

min_name, min_score = ('', 100)
for elem in arr:
    if elem[1] < min_score:
        min_name, min_score = elem[0], elem[1]

print(min_name, min_score)