n, m = tuple(map(int, input().split()))

a_arr = [0]*1000000
b_arr = [0]*1000000

distance_a = 0
st_sec_a = 0
for _ in range(n):
    direction, sec = tuple(input().split())
    sec = int(sec)
    if direction == 'L':
        for i in range(st_sec_a, st_sec_a+sec):
            distance_a -= 1
            a_arr[i] = distance_a
    else:
        for i in range(st_sec_a, st_sec_a+sec):
            distance_a += 1
            a_arr[i] = distance_a
    st_sec_a += sec

distance_b = 0
st_sec_b = 0
for _ in range(m):
    direction, sec = tuple(input().split())
    sec = int(sec)
    if direction == 'L':
        for i in range(st_sec_b, st_sec_b+sec):
            distance_b -= 1
            b_arr[i] = distance_b
    else:
        for i in range(st_sec_b, st_sec_b+sec):
            distance_b += 1
            b_arr[i] = distance_b
    st_sec_b += sec

# print(a_arr[:10])
# print(b_arr[:10])
res = 0
for i in range(1000000):
    if b_arr[i] == a_arr[i]:
        res = i
        break
print(res+1)