n = int(input())
arr = [
    tuple(input().split())
    for _ in range(n)
]

# no change: AB, A, B
# change: AB, A, B

a = 0
b = 0
curr = 'AB'
cnt = 0
for c, s in arr:
    if c == 'A':
        a += int(s)
    else:
        b += int(s)
    if a == b:
        if curr != 'AB':
            cnt += 1
            curr = 'AB'
    elif a > b:
        if curr != 'A':
            cnt += 1
            curr = 'A'
    else:
        if curr != 'B':
            cnt += 1
            curr = 'B'
print(cnt)