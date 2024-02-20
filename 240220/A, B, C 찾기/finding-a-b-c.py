arr = list(map(int, input().split()))
arr.sort()

abc = arr[-1]
bc = arr[-1] - arr[0]
# print(arr)

bc_arr = []
for i, elem in enumerate(arr):
    if elem == bc:
        bc_arr = arr[:i] + arr[i+1:]
        break
a = bc_arr[0]
b = bc_arr[1]
c = abc - (a+b)
print(a,b,c)