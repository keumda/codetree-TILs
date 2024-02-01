n, m = tuple(map(int, input().split()))

a_arr = [0]*2000
b_arr = [0]*2000

distance_a = 0
st_sec_a = 0
for _ in range(n):
    direction, sec = tuple(input().split())
    sec = int(sec)
    if direction == 'L':
        for i in range(st_sec_a, sec):
            a_arr[i] = distance_a
            distance_a -= 1
        st_sec_a += sec
    else:
        for i in range(st_sec_a, sec):
            a_arr[i] = distance_a
            distance_a += 1
        st_sec_a += sec

distance_b = 0
st_sec_b = 0
for _ in range(m):
    direction, sec = tuple(input().split())
    sec = int(sec)
    if direction == 'L':
        for i in range(st_sec_b, sec):
            b_arr[i] = distance_a
            distance_b -= 1
        st_sec_b += sec
    else:
        for i in range(st_sec_b, sec):
            b_arr[i] = distance_b
            distance_b += 1
        st_sec_b += sec

res = 0
for i in range(1000):
    if b_arr[i] == a_arr[i]:
        res = i
        break
print(res)