n, m = tuple(map(int, input().split()))

a_arr = []
b_arr = []
a_dist = 0
for _ in range(n):
    v, h = tuple(map(int, input().split()))
    for i in range(1, h+1):
        a_dist += v
        a_arr.append(a_dist)
b_dist = 0
for _ in range(m):
    v, h = tuple(map(int, input().split()))
    for i in range(1, h+1):
        b_dist += v
        b_arr.append(b_dist)

cnt = 0
is_a_faster = a_arr[0] > b_arr[0]
for i in range(len(a_arr)):
    if is_a_faster:
        # print(a_arr[i], b_arr[i], is_a_faster, b_arr[i] >= a_arr[i])
        if b_arr[i] > a_arr[i]:
            cnt += 1
            is_a_faster = False
        
    else:
        # print(a_arr[i], b_arr[i], is_a_faster, b_arr[i] <= a_arr[i])
        if b_arr[i] < a_arr[i]:
            cnt += 1
            is_a_faster = True
        

# print(a_arr)
# print(b_arr)
print(cnt)