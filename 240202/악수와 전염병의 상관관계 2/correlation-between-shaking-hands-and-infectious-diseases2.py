total_n, k, infected_n, handshake_t = tuple(map(int, input().split()))

devlopers_k = [0]*(total_n+1)
devlopers_k[infected_n] = k
devlopers_infected = [0]*(total_n+1)
devlopers_infected[infected_n] = 1

t_arr = []
for _ in range(handshake_t):
    t = tuple(map(int, input().split()))
    t_arr.append(t)
t_arr.sort(key = lambda x:x[0])

for elem in t_arr:
    t, x, y = elem
    if devlopers_infected[x] == 1 and devlopers_k[x] > 0:
        devlopers_k[x] -= 1
        if devlopers_infected[y] != 1:
            devlopers_k[y] = k
        devlopers_infected[y] = 1
        
    elif devlopers_infected[y] == 1 and devlopers_k[y] > 0:
        devlopers_k[y] -= 1
        if devlopers_infected[x] != 1:
            devlopers_k[x] = k
        devlopers_infected[x] = 1
    # print(devlopers_infected, devlopers_k)

for elem in devlopers_infected[1:]:
    print(elem, end='')