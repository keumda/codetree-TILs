n = int(input())
arr = list(map(int, input().split()))

min_idx = 0
arr_min = 100
for i, elem in enumerate(arr):
    if elem < arr_min:
        arr_min = elem
        min_idx = i
# print(arr_min)
# case 1. exist
# case 2. not exist
# case 3. more than 1

second_min = 101
second_min_idx = 0
is_possible = False
for j, elem in enumerate(arr):
    if elem > arr_min:
        # print(elem, second_min, second_min_idx)
        if elem <= second_min:
            if elem == second_min:
                is_possible = False
                second_min_idx = -1
            else:
                is_possible = True
                second_min = elem
                second_min_idx = j
    # print(elem, is_possible, second_min)
if is_possible:
    print(second_min_idx+1)
else:
    print(-1)