n, m = tuple(map(int, input().split()))

a_arr = [0]*1000000
b_arr = [0]*1000000

a_dist = 0
a_t = 1
for _ in range(n):
    t, d = tuple(input().split())
    t = int(t)
    if d == 'L':
        for i in range(t):
            a_dist -= 1
            a_arr[a_t] = a_dist
            a_t += 1  
    else:
        for i in range(t):
            a_dist += 1
            a_arr[a_t] = a_dist
            a_t += 1  

b_dist = 0
b_t = 1    
for _ in range(m):
    t, d = tuple(input().split())
    t = int(t)
    if d == 'L':
        for i in range(t):
            b_dist -= 1
            b_arr[b_t] = b_dist
            b_t += 1  
    else:
        for i in range(t):
            b_dist += 1
            b_arr[b_t] = b_dist
            b_t += 1  

cnt = 0
is_a_longer = True
if a_t < b_t:
    is_a_longer = False

for i in range(min(a_t, b_t), max(a_t, b_t)):
    if is_a_longer:
        b_arr[i] = b_dist
    else:
        a_arr[i] = a_dist

for i in range(1, max(a_t, b_t)):
    if a_arr[i] == b_arr[i] and a_arr[i-1] != b_arr[i-1]:
        cnt += 1
print(cnt)