dist = int(input())

min_time = 0
d = dist // 2
v = 1
while d >= 0:
    d = d - v
    v += 1
    min_time += 1
    # print(d, v)
print(min_time*2)