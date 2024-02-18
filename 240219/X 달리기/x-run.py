dist = int(input())

t = 0
v = 0
total_d = 0
while True:
    # print(t, v, total_d)
    v += 1
    total_d += v
    t += 1
    if total_d > dist//2:
        break
    
print(t+v)