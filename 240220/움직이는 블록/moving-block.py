n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

target_n = sum(arr) // n
cnt = 0
for elem in arr:
    if elem > target_n:
        cnt += elem - target_n
    # print(target_n, elem, cnt)
print(cnt)