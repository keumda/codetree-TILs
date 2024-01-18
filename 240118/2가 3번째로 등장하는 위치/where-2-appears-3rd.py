n = int(input())
arr = list(map(int, input().split()))

two_cnt = 0
for i, elem in enumerate(arr):
    if elem == 2:
        two_cnt += 1
        if two_cnt == 3:
            print(i+1)
            break