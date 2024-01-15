rows = 2
cols = 4

r_avg = []
c_avg = [0]*cols
total = 0

arr = [list(map(int, input().split())) for i in range(rows)]

for idx, i in enumerate(arr):
     r_avg.append(sum(i))
     for jidx, j in enumerate(i):
        total = total + j
        c_avg[jidx] = c_avg[jidx] + j

for i in r_avg:
    print(round(i/cols, 2), end=' ')
print()
for i in c_avg:
    print(round(i/rows, 2), end=' ')
print()
print(round(total/(rows*cols), 2))