n = int(input())
times = [
    tuple(map(int, input().split()))
    for t in range(n)
]

max_time = 0
for i in range(n):
    t_arr = [0]*1000
    s = 0
    for j in range(n):
        if j != i:
            for k in range(times[j][0], times[j][1]):
                t_arr[k] = 1
            # print(times[j][0], times[j][1], t_arr[:10])
            s = sum(t_arr)
            max_time = max(s, max_time)
print(max_time)