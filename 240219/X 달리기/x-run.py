dist = int(input())

t = 0
v = 0
total_d = 0
increase = 0
while True:
    if total_d >= dist:
        break
    if increase == 0:
        v += 1
    elif increase == 1:
        v -= 1
    else:
        v = v
    total_d += v
    t += 1
    # print(t, v, total_d)
    if total_d >= dist//2:
        increase = 1
    if v == 1 and total_d == (dist - 1):
        increase = 2

    
print(t)