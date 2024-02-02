n, m = tuple(map(int, input().split()))

a_arr = [0] * 1000001
b_arr = [0] * 1000001

a_dist = 0
a_t = 1
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for i in range(t):
        a_dist += v
        a_arr[a_t] = a_dist
        a_t += 1
b_dist = 0
b_t = 1
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for i in range(t):
        b_dist += v
        b_arr[b_t] = b_dist
        b_t += 1

honor_arr = []
for i in range(0, a_t):
    # print(a_arr[i], b_arr[i])
    if a_arr[i] > b_arr[i]:
        honor_arr.append('A')
    elif a_arr[i] < b_arr[i]:
        honor_arr.append('B')
    else:
        honor_arr.append('AB')

cnt = 0
# print(honor_arr, len(honor_arr), a_t)
for i in range(1, len(honor_arr)):
    if honor_arr[i-1] != honor_arr[i]:
        cnt += 1
print(cnt)